import math, random
import numpy as np

# Change WORKING_DIRECTORY and PACKAGE to run on local device
WORKING_DIRECTORY = "C:/Users/bfrem/Documents/CloudComputing/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/DatacenterTopologies"
PACKAGE = "inet.examples.inet.DatacenterTopologies"

IMPORTS = [
    "inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator",
    "inet.node.inet.Router",
    "inet.node.inet.StandardHost",
    "ned.DatarateChannel"
]

DEFAULT_CHANNEL = "defaultline"
DEFAULT_LINE_PARAMS = {
    "delay": "0.1us",
    "datarate": "1Gbps",
    "per": "0"
}

TAB = "    "

ROUTER_NED = "Router"
ROUTER_TYPE = "Router"
ROUTER_SIZE = "s"
ROUTER_ICON = "abstract/router"

STANDARD_HOST_NED = "StandardHost"
CLIENT_TYPE = "Client"
SERVER_TYPE = "Server"
STANDARD_HOST_SIZE = "s"
CLIENT_ICON = "device/laptop"
SERVER_ICON = "device/server"

SERVER_PORT = 1100
REQUEST_SIZE = 1300
RESPONSE_SIZE = 20
SIMULATION_TIME = 1000

class Connection:
    def __init__(self, gate_strings, channel):
        assert len(gate_strings) == 2
        self._gates = sorted(gate_strings)
        self._channel = channel
    
    def ned_connection(self):
        return f"{self._gates[0]} <--> {self._channel} <--> {self._gates[1]};"

class Flow:
    def __init__(self, src, dest, send_amount, start_delay):
        assert (send_amount > 0)
        self._src = src
        self._dest = dest
        self._num_packets = math.ceil(send_amount/REQUEST_SIZE)
        self._start_delay = int(start_delay)
    
    def ini_flow(self, app_idx):
        root = f"**.{self._src}.app[{app_idx}]"

        ini_str = ""
        ini_str += f"{root}.typename = \"TcpBasicClientApp\"\n"
        ini_str += f"{root}.localAddress = \"\"\n"
        ini_str += f"{root}.connectAddress = \"{self._dest}\"\n"
        ini_str += f"{root}.connectPort = {SERVER_PORT}\n"
        ini_str += f"{root}.startTime = {self._start_delay}s\n"
        ini_str += f"{root}.idleInterval = {SIMULATION_TIME}s\n"
        ini_str += f"{root}.requestLength = {REQUEST_SIZE}B\n"
        ini_str += f"{root}.replyLength = {RESPONSE_SIZE}B\n"
        ini_str += f"{root}.thinkTime = 0s\n"
        ini_str += f"{root}.numRequestsPerSession = {self._num_packets}\n"
        ini_str += "\n"

        return ini_str


class Line:
    def __init__(self, channel=DEFAULT_CHANNEL, params=DEFAULT_LINE_PARAMS):
        self._channel = channel
        self._params = params
    
    def ned_type(self):
        return (
            f"channel {self._channel} extends DatarateChannel" +
            " { " +
            "; ".join([f"{k} = {v}" for (k, v) in self._params.items()]) +
            "; }"
        )
    
    def get_channel(self):
        return self._channel

class Configurator:
    def __init__(self, x, y, name="configurator"):
        self._name = name
        self._x = int(x)
        self._y = int(y)
        self._size = "s"
        self._icon = "block/cogwheel"
    
    def ned_submodule(self):
        return (
            f"{self._name}: Ipv4NetworkConfigurator" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            " }"
        )

class Node:
    def __init__(self, name, node_type, x, y):
        assert node_type in [ROUTER_TYPE, CLIENT_TYPE, SERVER_TYPE]
        self._type = node_type
        self._name = name
        self._ned = ROUTER_NED if node_type == ROUTER_TYPE else STANDARD_HOST_NED
        self._icon = ROUTER_ICON
        if node_type == CLIENT_TYPE:
            self._icon = CLIENT_ICON
        elif node_type == SERVER_TYPE:
            self._icon = SERVER_ICON
        self._size = "s"
        self._x = int(x)
        self._y = int(y)
        self._links = []
        self._flows = []
    
    @staticmethod
    def encode_link(link):
        return f"{link[0]}__{link[1]}__{link[2]}"
    
    @staticmethod
    def connect(node_a, node_b, channel=DEFAULT_CHANNEL, index=0):
        node_a.add_link(node_b.get_name(), channel, index)
        node_b.add_link(node_a.get_name(), channel, index)

    def add_link(self, other="", channel="", index=0, link=None):
        link = link if link else (other, channel, index)
        if link not in self._links:
            self._links.append(link)
            # print(f"  {self._name} connected with {link[0]} --- current links: {self._links}")
            return (self._name, channel, index)
        else:
            # print(f"  {self._name} could not connect with {link[0]}")
            return None
    
    def remove_link(self, other="", channel=DEFAULT_CHANNEL, index=0, link=None):
        link = link if link else (other, channel, index)
        if link not in self._links:
            return None
        else:
            self._links.remove(link)
            return (self._name, channel, index)
    
    def sort_links(self):
        self._links.sort(key=Node.encode_link)
    
    def is_connected_to(self, other):
        return any(link[0] == other._name for link in self._links) or self._name == other._name
    
    def add_flow(self, dest, amount, delay):
        self._flows.append(Flow(self._name, dest.get_name(), amount, delay))

    def get_flows(self):
        ini_str = f"**.{self._name}.numApps = {len(self._flows)}\n"
        for index, flow in enumerate(self._flows):
            ini_str += flow.ini_flow(index)
        return ini_str
    
    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    
    def get_num_flows(self):
        return len(self._flows)

    def get_num_gates(self):
        return len(self._links)
    
    def get_gate_num(self, link):
        return self._links.index(link)
    
    def get_connections(self, node_map):
        connections = []
        # print(self._name, "---", self._links)
        for my_link in self._links:
            my_gate = f"{self._name}.pppg[{self.get_gate_num(my_link)}]"

            other_name, channel, index = my_link
            other_link = (self._name, channel, index)
            other = node_map[other_name]
            other_gate = f"{other_name}.pppg[{other.get_gate_num(other_link)}]"

            # print(my_link, other_link)
            connections.append(Connection([my_gate, other_gate], channel).ned_connection())
        # print(connections, "---", set(connections))
        return set(connections)

    def ned_submodule(self):
        return (
            f"{self._name}: {self._ned}" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            f" gates: pppg[{self.get_num_gates()}];" +
            " }"
        )

class Network:
    def __init__(self, name, package=PACKAGE, imports=IMPORTS, width=400, height=300):
        self._name = name
        self._package = package
        self._imports = imports
        self._width = int(width)
        self._height = int(height)
        self._node_map = {}
        self._configurator = Configurator(50, 50)
        self._lines = []
        self._flows = []
    
    def get_name(self):
        return self._name
    
    def initialize(self):
        self._lines = [Line()]
        channel = self._lines[0].get_channel()
        self._node_map = {}
        self._node_map["router"] = Node("router", ROUTER_TYPE, 0.5 * self._width, self._height / 2)
        self._node_map["client"] = Node("client", CLIENT_TYPE, 0.25 * self._width, self._height / 2)
        self._node_map["server"] = Node("server", SERVER_TYPE, 0.75 * self._width, self._height / 2)

        Node.connect(self._node_map["client"], self._node_map["router"], channel)
        Node.connect(self._node_map["server"], self._node_map["router"], channel)

        self._node_map["client"].add_flow(self._node_map["server"], 1000000, 0)

        return self

    def ned_connections(self):
        # alphabetize links :)
        for node in self._node_map.values():
            node.sort_links()

        connections = set([])
        for node in self._node_map.values():
            # print(f"{node.get_name()} +++ {node.get_connections(self._node_map)}")
            connections = connections.union(node.get_connections(self._node_map))
        return sorted(list(connections))

    def ned_submodules(self):
        submodules = set([self._configurator.ned_submodule()])
        for node in self._node_map.values():
            submodules.add(node.ned_submodule())
        return sorted(list(submodules))

    def create_ned_file(self):
        ned_str = ""

        ned_str += f"package {self._package};"
        ned_str += "\n\n"
        ned_str += "\n".join([f"import {imp};" for imp in self._imports])
        ned_str += "\n\n"

        ned_str += f"network {self._name}\n"
        ned_str += "{\n"

        ned_str += f"{TAB}parameters:\n"
        ned_str += f"{TAB}{TAB}@display(\"bgb={self._width},{self._height}\");"
        ned_str += "\n"

        ned_str += f"{TAB}types:\n"
        ned_str += "\n".join([f"{TAB}{TAB}{line.ned_type()}" for line in self._lines])
        ned_str += "\n"

        ned_str += f"{TAB}submodules:\n"
        ned_str += "\n".join([f"{TAB}{TAB}{mod}" for mod in self.ned_submodules()])
        ned_str += "\n"

        ned_str += f"{TAB}connections:\n"
        ned_str += "\n".join([f"{TAB}{TAB}{conn}" for conn in self.ned_connections()])
        ned_str += "\n"

        ned_str += "}"

        fd = open(f"{WORKING_DIRECTORY}/{self._name}.ned", "w")
        fd.write(ned_str)
        fd.close()

        return ned_str

    def create_ini_file(self):
        ini_str = ""

        ini_str += "[General]\n"
        ini_str += f"network = {self._name}\n\n"

        ini_str += "sim-time-limit = 1000s\n"
        ini_str += "simtime-resolution = us\n"
        ini_str += "total-stack = 7MiB\n"
        ini_str += "\n"

        ini_str += "# For TCP\n"
        ini_str += "**.tcp.mss = 1400\n"
        # Options: "TcpVegas","TcpWestwood","TcpNewReno","TcpReno","TcpTahoe","TcpNoCongestionControl"
        ini_str += "**.tcp.tcpAlgorithmClass = \"TcpReno\"\n"
        ini_str += "**.tcp.crcMode = \"computed\"\n"
        ini_str += "\n"

        ini_str += "# For router\n"
        ini_str += "**.ppp[*].ppp.queue.typename = \"DropTailQueue\"\n"
        ini_str += "**.ppp[*].ppp.queue.packetCapacity = 100\n"
        ini_str += "\n"

        for name, node in self._node_map.items():
            if node.get_type() == SERVER_TYPE:
                root = f"**.{name}"
                ini_str += f"# Setup TCP server \"{node.get_name()}\"\n"
                ini_str += f"{root}.numApps = 1\n"
                ini_str += f"{root}.app[0].typename = \"TcpGenericServerApp\"\n"
                ini_str += f"{root}.app[0].localAddress = \"\"\n"
                ini_str += f"{root}.app[0].localPort = {SERVER_PORT}\n"
                ini_str += f"{root}.app[0].replyDelay = 0s\n"
                ini_str += "\n"

        for name, node in self._node_map.items():
            if node.get_type() == CLIENT_TYPE:
                ini_str += f"# Setup TCP client \"{node.get_name()}\"\n"
                ini_str += node.get_flows()
                if (node.get_num_flows() == 0):
                    ini_str += "\n"

        ini_str += "**.app[*].dataTransferMode = \"object\"\n"

        fd = open(f"{WORKING_DIRECTORY}/{self._name}.ini", "w")
        fd.write(ini_str)
        fd.close()

        return ini_str

class FatTree(Network):
    def __init__(self, name, switch_degree, package=PACKAGE, imports=IMPORTS, width=800, height=500):
        super().__init__(name, package, imports, width, height)
        assert switch_degree % 4 == 0
        assert switch_degree >= 4
        self._k = switch_degree
        self._servers = []
        self._clients = []

    def initialize(self):
        def z(num, n=2):
            return f"{num}".zfill(n)

        self._lines = [Line()]
        channel = self._lines[0].get_channel()

        for i in range(self._k ** 2 // 2):
            self._node_map[f"agg_{z(i)}"] = Node(f"agg_{z(i)}", ROUTER_TYPE, (i + 0.5) * self._width / (self._k ** 2 / 2), 200)
            self._node_map[f"edge_{z(i)}"] = Node(f"edge_{z(i)}", ROUTER_TYPE, (i + 0.5) *  self._width / (self._k ** 2 / 2), 300)
        for i in range(self._k ** 2 // 4):
            self._node_map[f"core_{z(i)}"] = Node(f"core_{z(i)}", ROUTER_TYPE, (i + 0.5) * self._width / (self._k ** 2 / 4), 100)
        for i in range(self._k ** 3 // 4):
            node_type = SERVER_TYPE if i % 4 == 3 else CLIENT_TYPE
            self._node_map[f"host_{z(i)}"] = Node(f"host_{z(i)}", node_type, (i + 0.5) * self._width / (self._k ** 3 / 4), 400)
            if i % 4 == 3:
                self._servers.append(self._node_map[f"host_{z(i)}"])
            else:
                self._clients.append(self._node_map[f"host_{z(i)}"])

        # Connect hosts to edge routers
        edge_index = 0
        edge_counter = 0
        for i in range(self._k ** 3 // 4):
            Node.connect(self._node_map[f"host_{z(i)}"], self._node_map[f"edge_{z(edge_index)}"], channel)
            edge_counter += 1
            if edge_counter == self._k // 2:
                edge_index += 1
                edge_counter = 0
        
        # Connect edge to aggregate
        for i in range(self._k ** 2 // 2):
            group = i // (self._k // 2)
            for j in range(group * self._k // 2, (group + 1) * self._k // 2):
                Node.connect(self._node_map[f"edge_{z(i)}"], self._node_map[f"agg_{z(j)}"], channel)

        # Connect aggreagte to core
        core_counter = 0
        for i in range(self._k ** 2 // 2):
            for j in range(self._k // 2):
                Node.connect(self._node_map[f"agg_{z(i)}"], self._node_map[f"core_{z(core_counter)}"], channel)
                core_counter = (core_counter + 1) % (self._k ** 2 // 4)
        
        generate_random_flows(self._clients, self._servers, 10)

        return self

class Jellyfish(Network):
    def __init__(self, name, num_switches, ports_per_switch, internal_ports, package=PACKAGE, imports=IMPORTS, width=800, height=500):
        super().__init__(name, package, imports, width, height)
        assert ports_per_switch > internal_ports
        self._n = num_switches  # number of routers
        self._k = ports_per_switch  # number of ports per router
        self._r = internal_ports  # number of ports connecting to other routers
        self._servers = []
        self._clients = []

    def initialize(self):
        def z(num, n=2):
            return f"{num}".zfill(n)

        self._lines = [Line()]
        channel = self._lines[0].get_channel()

        for i in range(self._n):
            self._node_map[f"core_{z(i)}"] = Node(f"core_{z(i)}", ROUTER_TYPE, 
                self._width / 2 + 150 * math.cos(2 * math.pi * i / self._n), 
                self._height / 2 + 150 * math.sin(2 * math.pi * i / self._n))

        num_hosts = self._n * (self._k - self._r)
        slide = 0 if self._k == self._r + 1  else 0.5
        for i in range(num_hosts):
            node_type = SERVER_TYPE if i % 4 == 3 else CLIENT_TYPE
            self._node_map[f"host_{z(i)}"] = Node(f"host_{z(i)}", node_type, 
                self._width / 2 + 200 * math.cos(2 * math.pi * (i - slide) / num_hosts), 
                self._height / 2 + 200 * math.sin(2 * math.pi * (i - slide) / num_hosts))
            if i % 4 == 3:
                self._servers.append(self._node_map[f"host_{z(i)}"])
            else:
                self._clients.append(self._node_map[f"host_{z(i)}"])

        # make sure there is at least one cycle in the graph
        rands = [idx for idx in range(self._n)]
        random.shuffle(rands)
        # print(rands)
        for i in range(self._n):
            Node.connect(self._node_map[f"core_{z(rands[i])}"], self._node_map[f"core_{z(rands[(i + 1) % self._n])}"], channel)

        for i in range(self._n):
            core_node = self._node_map[f"core_{z(i)}"]
            if (self._r == core_node.get_num_gates()):
                continue  # router is already fully connected
            potential_neighbors = [node for node in filter(lambda node: node.get_type() == ROUTER_TYPE, self._node_map.values())]
            potential_neighbors = [node for node in filter(lambda node: node.get_num_gates() < self._r, potential_neighbors)]
            potential_neighbors = [node for node in filter(lambda node: not core_node.is_connected_to(node), potential_neighbors)]

            neighbors = potential_neighbors
            if (self._r - core_node.get_num_gates() <= len(potential_neighbors)):
                neighbors = random.sample(potential_neighbors, self._r - core_node.get_num_gates())
            else:
                print(f"Not enough potential neighbors for node {i}")
            
            for neighbor in neighbors:
                Node.connect(core_node, neighbor, channel)
        
        for i in range(num_hosts):
            host_node = self._node_map[f"host_{z(i)}"]
            router_node = self._node_map[f"core_{z(int(i / (self._k - self._r)))}"]
            Node.connect(host_node, router_node, channel)
        
        generate_random_flows(self._clients, self._servers, 10)

        return self

class VL2(Network):
    def __init__(self, name, ports_per_core_switch, ports_per_aggregate_switch, hosts_per_tor, package=PACKAGE, imports=IMPORTS, width=800, height=500):
        super().__init__(name, package, imports, width, height)
        assert ports_per_core_switch % 4 == 0
        self._c = ports_per_core_switch  # degree of core routers
        self._a = ports_per_aggregate_switch  # degree of aggregate routers
        self._s = hosts_per_tor  # servers per ToR
        self._servers = []
        self._clients = []

    def initialize(self):
        def z(num, n=2):
            return f"{num}".zfill(n)

        self._lines = [Line()]
        channel = self._lines[0].get_channel()

        for i in range(self._a // 2):
            self._node_map[f"core_{z(i)}"] = Node(f"core_{z(i)}", ROUTER_TYPE, 
                self._width * (i + 0.5) / (self._a // 2), 100)
        
        for i in range(self._c):
            self._node_map[f"agg_{z(i)}"] = Node(f"agg_{z(i)}", ROUTER_TYPE, 
                self._width * (i + 0.5) / (self._c), 200)
        
        for i in range(self._a * self._c // 4):
            self._node_map[f"tor_{z(i)}"] = Node(f"tor_{z(i)}", ROUTER_TYPE, 
                self._width * (i + 0.5) / (self._a * self._c // 4), 300)

        for i in range(self._s * self._a * self._c // 4):
            node_type = SERVER_TYPE if i % 4 == 3 else CLIENT_TYPE
            self._node_map[f"host_{z(i)}"] = Node(f"host_{z(i)}", node_type, 
                self._width * (i + 0.5) / (self._s * self._a * self._c // 4), 400)
            if i % 4 == 3:
                self._servers.append(self._node_map[f"host_{z(i)}"])
            else:
                self._clients.append(self._node_map[f"host_{z(i)}"])

        # Connect hosts to tor routers
        tor_index = 0
        tor_counter = 0
        for i in range(self._s * self._a * self._c // 4):
            Node.connect(self._node_map[f"host_{z(i)}"], self._node_map[f"tor_{z(tor_index)}"], channel)
            tor_counter += 1
            if tor_counter == self._s:
                tor_index += 1
                tor_counter = 0

        # Connect tor to aggregate
        for i in range(self._a * self._c // 4):
            group = i // (self._a // 2)
            for j in range(group * 2, (group + 1) * 2):
                Node.connect(self._node_map[f"tor_{z(i)}"], self._node_map[f"agg_{z(j)}"], channel)

        # Connect aggregate to core
        for i in range(self._c):
            for j in range(self._a // 2):
                Node.connect(self._node_map[f"agg_{z(i)}"], self._node_map[f"core_{z(j)}"], channel)
        
        generate_random_flows(self._clients, self._servers, 10)

        return self

flows = []
def generate_random_flows(clients, servers, n):
    if len(flows) == 0:
        for i in range(n):
            p = np.random.normal(4, 1)
            while p < 3:
                p = np.random.normal(4, 1)
            flows.append(10 ** p)
    for i in range(n):
        client = random.sample(clients, 1)[0]
        server = random.sample(servers, 1)[0]
        client.add_flow(server, flows[i], 0)

def main():
    random.seed(0)
    np.random.seed(0)

    network = Network(name="Default").initialize()
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    print(f"{ned_str}\n{ini_str}\n\n")

    network = FatTree(name="FatTree", switch_degree=4).initialize()
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    print(f"{ned_str}\n{ini_str}\n\n")

    network = Jellyfish(name="Jelly", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    print(f"{ned_str}\n{ini_str}\n\n")

    network = VL2(name="VL2", ports_per_core_switch=4, ports_per_aggregate_switch=4, hosts_per_tor=4).initialize()
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    print(f"{ned_str}\n{ini_str}")

    return



if __name__ == "__main__":
    main()