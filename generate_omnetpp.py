import math, random, copy
import numpy as np
import networkx as nx

WORKING_DIRECTORY = "C:/Users/bfrem/Documents/CloudComputing/omnetpp-5.7-windows-x86_64/omnetpp-5.7/samples/inet4/examples/inet/DatacenterTopologies"
GENERATED_FILES_DIR = "generated_files"

PACKAGE = "inet.examples.inet.DatacenterTopologies"

IMPORTS = [
    "inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator",
    "inet.node.inet.Router",
    "inet.node.inet.StandardHost",
    "ned.DatarateChannel",
    "inet.visualizer.integrated.IntegratedVisualizer"
]

DEFAULT_CHANNEL = "defaultline"
DEFAULT_LINE_PARAMS = {
    "delay": "1us",
    "datarate": "8Mbps",
    "per": "0"
}

INFINITE_CHANNEL = "infiniteline"
INFINITE_LINE_PARAMS = {
    "delay": "0s",
    "datarate": "1000Gbps",
    "per": "0"
}

TAB = "    "

SIZE_SMALL = "s"
SIZE_VERY_SMALL = "vs"

ICON_ROUTER = "abstract/router"
ICON_SOURCE = "block/source"
ICON_SINK = "block/sink"
ICON_PC = "device/pc"
ICON_LAPTOP = "device/laptop"
ICON_SERVER = "device/server"
ICON_CONFIGURATOR = "block/cogwheel"
ICON_VISUALIZER = "block/app"
ICON_SWITCH = "device/switch"

NED_CONFIGURATOR = "Ipv4NetworkConfigurator"
NED_VISUALIZER = "IntegratedVisualizer"
NED_ROUTER = "Router"
NED_STANDARD_HOST = "StandardHost"

"""
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
"""

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
    
    def get_endpoints(self):
        return (self._src, self._dest)

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
        self._icon = ICON_CONFIGURATOR
    
    def ned_submodule(self):
        return (
            f"{self._name}: Ipv4NetworkConfigurator" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            " }"
        )

class Visualizer:
    def __init__(self, x, y, name="visualizer"):
        self._name = name
        self._x = int(x)
        self._y = int(y)
        self._size = "s"
        self._icon = ICON_VISUALIZER
    
    def ned_submodule(self):
        return (
            f"{self._name}: IntegratedVisualizer" +
            " { parameters:" +
            f" @display(\"p={self._x},{self._y};i={self._icon};is={self._size}\");" +
            " }"
        )

class Node:
    def __init__(self, name, x, y):
        self._name = name
        self._size = "s"
        self._x = int(x)
        self._y = int(y)
        self._links = []
        self._flows = []
        self._ip_root = None
    
    @staticmethod
    def encode_link(link):
        return f"{link[0]}__{link[1]}__{link[2]}"
    
    @staticmethod
    def connect(node_a, node_b, channel=DEFAULT_CHANNEL, index=0):
        node_a.add_link(node_b.get_name(), channel, index)
        node_b.add_link(node_a.get_name(), channel, index)

    def get_nx_edges(self):
        return [(self._name, link[0]) for link in self._links]
    
    def gate_index_to(self, other):
        for i, link in enumerate(self._links):
            if link[0] == other.get_name():
                return i
        return -1

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

    def get_flows_ini_str(self):
        ini_str = f"**.{self._name}.numApps = {len(self._flows)}\n"
        for index, flow in enumerate(self._flows):
            ini_str += flow.ini_flow(index)
        return ini_str
    
    def get_flows_endpoints(self):
        return [flow.get_endpoints() for flow in self._flows]   

    def get_name(self):
        return self._name
    
    def get_ned(self):
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

class Router(Node):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self._ned = NED_ROUTER
        self._icon = ICON_ROUTER
        self._size = SIZE_SMALL

class Source(Node):
    def __init__(self, name, server_name, x, y):
        super().__init__(name, x, y)
        self._ned = NED_STANDARD_HOST
        self._icon = ICON_SOURCE
        self._size = SIZE_VERY_SMALL
        self._server_name = server_name
    
    def get_server_name(self):
        return self._server_name

class Sink(Node):
    def __init__(self, name, server_name, x, y):
        super().__init__(name, x, y)
        self._ned = NED_STANDARD_HOST
        self._icon = ICON_SINK
        self._size = SIZE_VERY_SMALL
        self._server_name = server_name
    
    def get_server_name(self):
        return self._server_name

class Server(Node):
    def __init__(self, name, x, y, source_coords=None, sink_coords=None):
        super().__init__(name, x, y)
        self._ned = NED_ROUTER
        self._icon = ICON_SERVER
        self._size = SIZE_SMALL
        if source_coords:
            self._source_coords = source_coords
        else:
            self._source_coords = (x - 25, y + 50)
        if sink_coords:
            self._sink_coords = sink_coords
        else:
            self._sink_coords = (x + 25, y + 50)
    
    def get_source_coords(self):
        return self._source_coords

    def get_sink_coords(self):
        return self._sink_coords

class Tor(Node):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self._ned = NED_ROUTER
        self._icon = ICON_SWITCH
        self._size = SIZE_SMALL

"""
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
"""

class RoutingAlgorithm:
    @staticmethod
    def get_nx_graph(network):
        G = nx.Graph()
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            G.add_node(node.get_name())
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            for edge in node.get_nx_edges():
                if not G.has_edge(*edge):
                    G.add_edge(*edge)
        return G

    @staticmethod
    def k_shortest_paths(G, source, target, k):
        paths = []
        for path in nx.shortest_simple_paths(G, source, target):
            if len(paths) < k:
                paths.append(path)
            else:
                break
        return paths
    
    @staticmethod
    def all_shortest_paths(G, source, target):
        paths = []
        min_path_length = 999
        for path in nx.shortest_simple_paths(G, source, target):
            if len(path) < min_path_length:
                min_path_length = len(path)
                paths.append(path)
            elif len(path) == min_path_length:
                paths.append(path)
            else:
                break
        return paths

    @staticmethod
    def xml_route(from_node, to_node, dest_node):
        from_gate_index = from_node.gate_index_to(to_node)
        to_gate_index = to_node.gate_index_to(from_node)
        return f"<route hosts='{from_node.get_name()}' destination='{dest_node._ip_root}.0.8' netmask='255.255.255.255' gateway='{to_node._ip_root}.{to_gate_index}.8' interface='ppp{from_gate_index}' metric='0'/>"

    @staticmethod
    def path_route_xml_generator(network, path_finder, flow_src, flow_dest):
        server_src = network._node_map[flow_src].get_server_name()
        server_dest = network._node_map[flow_dest].get_server_name()
        path = path_finder(server_src, server_dest)
        path.insert(0, flow_src)
        path.append(flow_dest)
        flow_dest_node = network._node_map[flow_dest]

        routes = [f"<!-- Route [ {', '.join(path)} ] -->"]
        for i in range(len(path) - 1):
            from_node = network._node_map[path[i]]
            to_node = network._node_map[path[i + 1]]
            routes.append(RoutingAlgorithm.xml_route(from_node, to_node, flow_dest_node))
        return routes

    @staticmethod
    def network_route_xml_generator(network, path_finder):
        routes = []
        # routes have the form below:
        # <route hosts="router0" destination="1.0.1.8" netmask="255.255.255.255" gateway="1.0.7.8" interface="ppp2" metric="0"/>
        for node in sorted(network._node_map.values(), key=lambda n: n.get_name()):
            for flow_src, flow_dest in node.get_flows_endpoints():
                routes.extend(RoutingAlgorithm.path_route_xml_generator(network, path_finder, flow_src, flow_dest))
                routes.extend(RoutingAlgorithm.path_route_xml_generator(network, path_finder, flow_dest, flow_src))
        return routes

    @staticmethod
    def ecmp_xml_routes(network):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        def path_finder(server_src, server_dest):
            server_src_dest = (server_src, server_dest) 
            if server_src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[server_src_dest] = RoutingAlgorithm.all_shortest_paths(graph, server_src_dest[0], server_src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[server_src_dest], 1)[0]
            return copy.deepcopy(randomly_selected_path)
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
    @staticmethod
    def ksp_xml_routes(network, k):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        def path_finder(server_src, server_dest):
            server_src_dest = (server_src, server_dest) 
            if server_src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[server_src_dest] = RoutingAlgorithm.k_shortest_paths(graph, server_src_dest[0], server_src_dest[1], k)
            randomly_selected_path = random.sample(shortest_paths_sets[server_src_dest], 1)[0]
            return copy.deepcopy(randomly_selected_path)
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
    @staticmethod
    def vlb_xml_routes(network):
        graph = RoutingAlgorithm.get_nx_graph(network)
        shortest_paths_sets = {}
        intermediate_nodes = [node for node in filter(lambda n: "intermediate" in n, graph.nodes)]
        def path_finder(server_src, server_dest):
            # Select a random intermeddiate node
            randomly_selected_intermediate = random.sample(intermediate_nodes, 1)[0]

            # ECMP routing from source to intermeddiate node
            src_dest = (server_src, randomly_selected_intermediate)
            if src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[src_dest] = RoutingAlgorithm.all_shortest_paths(graph, src_dest[0], src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[src_dest], 1)[0]
            path = copy.deepcopy(randomly_selected_path)
            path = path[:-1]  # remove last element because so that intermeddiate node isn't dupliacted

            # ECMP routing from intermediate node to dest
            src_dest = (randomly_selected_intermediate, server_dest)
            if src_dest not in shortest_paths_sets.keys():
                shortest_paths_sets[src_dest] = RoutingAlgorithm.all_shortest_paths(graph, src_dest[0], src_dest[1])
            randomly_selected_path = random.sample(shortest_paths_sets[src_dest], 1)[0]
            path.extend(copy.deepcopy(randomly_selected_path))
            return path
        return RoutingAlgorithm.network_route_xml_generator(network, path_finder)
    
class Network:
    def __init__(self, name, package=PACKAGE, imports=IMPORTS, width=800, height=500, use_visualizer=False):
        self._name = name
        self._package = package
        self._imports = imports
        self._width = int(width)
        self._height = int(height)
        self._node_map = {}
        self._configurator = Configurator(50, 50)
        self._visualizer = Visualizer(50, 100) if use_visualizer else None
        self._source_sink_counter = 0
        self._lines = []
        self._flows = []
        self._categorized_host_names = None
    
    def get_name(self):
        return self._name

    def add_node(self, node):
        if node.get_name() in self._node_map.keys():
            print(f"ERROR: {node.get_name()} is already in map keys: {list(self._node_map.keys())}")
            return
        self._node_map[node.get_name()] = node
    
    def initialize(self):
        self._lines = [
            Line(DEFAULT_CHANNEL, DEFAULT_LINE_PARAMS), 
            Line(INFINITE_CHANNEL, INFINITE_LINE_PARAMS)
        ]
        self._node_map = {}
        self.add_node(Server("host_0", 1 / 4 * self._width, self._height / 2))
        self.add_node(Server("host_1", 3 / 4 * self._width, self._height / 2))
        self.add_node(Router("core_0", 2 / 4 * self._width, self._height * 1 / 4))
        self.add_node(Router("core_1", 2 / 4 * self._width, self._height * 2 / 4))
        self.add_node(Router("core_2", 2 / 4 * self._width, self._height * 3 / 4))

        Node.connect(self._node_map["host_0"], self._node_map["core_0"], DEFAULT_CHANNEL)
        Node.connect(self._node_map["host_0"], self._node_map["core_1"], DEFAULT_CHANNEL)
        Node.connect(self._node_map["host_0"], self._node_map["core_2"], DEFAULT_CHANNEL)
        Node.connect(self._node_map["host_1"], self._node_map["core_0"], DEFAULT_CHANNEL)
        Node.connect(self._node_map["host_1"], self._node_map["core_1"], DEFAULT_CHANNEL)
        Node.connect(self._node_map["host_1"], self._node_map["core_2"], DEFAULT_CHANNEL)

        # self._node_map["client"].add_flow(self._node_map["host"], 1000000, 0)

        self.add_flow(self._node_map["host_0"], self._node_map["host_1"], 1000000, 0)
        self.add_flow(self._node_map["host_0"], self._node_map["host_1"], 1000000, 0)
        self.add_flow(self._node_map["host_0"], self._node_map["host_1"], 1000000, 0)

        return self

    def get_categorized_host_names(self):
        if self._categorized_host_names:
            return self._categorized_host_names
        self._categorized_host_names = {}
        for node_name in self._node_map.keys():
            node_type = node_name.split("_")[0]
            if node_type not in self._categorized_host_names:
                self._categorized_host_names[node_type] = []
            self._categorized_host_names[node_type].append(node_name)
        for node_type in self._categorized_host_names.keys():
            self._categorized_host_names[node_type] = sorted(self._categorized_host_names[node_type])
        return self._categorized_host_names

    def add_flow(self, send, recv, amount, start):
        if isinstance(send, str):
            send = self._node_map[send]
        if isinstance(recv, str):
            recv = self._node_map[recv]
        source_name = f"source_{self._source_sink_counter}"
        sink_name = f"sink_{self._source_sink_counter}"
        self._source_sink_counter += 1
        source = Source(source_name, send._name, *send.get_source_coords())
        Node.connect(source, send, INFINITE_CHANNEL)
        sink = Sink(sink_name, recv._name, *recv.get_sink_coords())
        Node.connect(sink, recv, INFINITE_CHANNEL)
        source.add_flow(sink, amount, start)
        self.add_node(source)
        self.add_node(sink)

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
        if self._visualizer:
            submodules.add(self._visualizer.ned_submodule())
        for node in self._node_map.values():
            submodules.add(node.ned_submodule())
        return sorted(list(submodules))

    def xml_interfaces(self):
        interfaces = []
        ip_major = 1
        ip_minor = 0
        for node in sorted(self._node_map.values(), key=lambda n: n.get_name()):
            node._ip_root = f"{ip_major}.{ip_minor}"
            ip_minor += 1
            if ip_minor == 256:
                ip_minor = 0
                ip_major += 1
            for i in range(node.get_num_gates()):
                interfaces.append(f"<interface hosts='{node.get_name()}' names='ppp{i}' address='{node._ip_root}.{i}.8' netmask='255.255.255.x'/>")
                
        interfaces.append(f"<interface hosts='**' address='255.x.x.x' netmask='255.255.255.x'/>")
        return interfaces

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

        fd = open(f"{GENERATED_FILES_DIR}/{self._name}.ned", "w")
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

        ini_str += "# Configurator settings\n"
        ini_str += f"*.configurator.config = xmldoc(\"{self._name}.xml\")\n"
        ini_str += "\n"

        if (self._visualizer):
            ini_str += "*.configurator.dumpAddresses = true\n"
            ini_str += "*.configurator.dumpTopology = true\n"
            ini_str += "*.configurator.dumpLinks = true\n"
            ini_str += "*.configurator.dumpRoutes = true\n"

            ini_str += "# Visualizer settings\n"
            ini_str += "*.visualizer.*.interfaceTableVisualizer.displayInterfaceTables = true\n"
            ini_str += "\n"

        for name, node in self._node_map.items():
            if isinstance(node, Sink):
                root = f"**.{name}"
                ini_str += f"# Setup TCP server \"{node.get_name()}\"\n"
                ini_str += f"{root}.numApps = 1\n"
                ini_str += f"{root}.app[0].typename = \"TcpGenericServerApp\"\n"
                ini_str += f"{root}.app[0].localAddress = \"\"\n"
                ini_str += f"{root}.app[0].localPort = {SERVER_PORT}\n"
                ini_str += f"{root}.app[0].replyDelay = 0s\n"
                ini_str += "\n"

        for name, node in self._node_map.items():
            if isinstance(node, Source):
                ini_str += f"# Setup TCP client \"{node.get_name()}\"\n"
                ini_str += node.get_flows_ini_str()
                if (node.get_num_flows() == 0):
                    ini_str += "\n"

        ini_str += "**.app[*].dataTransferMode = \"object\"\n"

        fd = open(f"{WORKING_DIRECTORY}/{self._name}.ini", "w")
        fd.write(ini_str)
        fd.close()

        fd = open(f"{GENERATED_FILES_DIR}/{self._name}.ini", "w")
        fd.write(ini_str)
        fd.close()

        return ini_str
    
    def create_xml_file(self):
        xml_str = ""
        xml_str += "<config>\n"
        for interface in self.xml_interfaces():
            xml_str += f"{TAB}{interface}\n"
        print("Generating Routes")
        for route in RoutingAlgorithm.ecmp_xml_routes(self):
            xml_str += f"{TAB}{route}\n"
        xml_str += "</config>\n"
        fd = open(f"{WORKING_DIRECTORY}/{self._name}.xml", "w")
        fd.write(xml_str)
        fd.close()

        fd = open(f"{GENERATED_FILES_DIR}/{self._name}.xml", "w")
        fd.write(xml_str)
        fd.close()

        return xml_str

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

        self._lines = [
            Line(DEFAULT_CHANNEL, DEFAULT_LINE_PARAMS), 
            Line(INFINITE_CHANNEL, INFINITE_LINE_PARAMS)
        ]

        for i in range(self._k ** 2 // 4):
            self._node_map[f"core_{z(i)}"] = Router(f"core_{z(i)}", (i + 0.5) * self._width / (self._k ** 2 / 4), 100)
        for i in range(self._k ** 2 // 2):
            self._node_map[f"agg_{z(i)}"] = Router(f"agg_{z(i)}", (i + 0.5) * self._width / (self._k ** 2 / 2), 200)
            self._node_map[f"edge_{z(i)}"] = Router(f"edge_{z(i)}", (i + 0.5) *  self._width / (self._k ** 2 / 2), 300)
        for i in range(self._k ** 3 // 4):
            self._node_map[f"host_{z(i)}"] = Server(f"host_{z(i)}", (i + 0.5) * self._width / (self._k ** 3 / 4), 400)

        # Connect hosts to edge routers
        edge_index = 0
        edge_counter = 0
        for i in range(self._k ** 3 // 4):
            Node.connect(self._node_map[f"host_{z(i)}"], self._node_map[f"edge_{z(edge_index)}"], DEFAULT_CHANNEL)
            edge_counter += 1
            if edge_counter == self._k // 2:
                edge_index += 1
                edge_counter = 0
        
        # Connect edge to aggregate
        for i in range(self._k ** 2 // 2):
            group = i // (self._k // 2)
            for j in range(group * self._k // 2, (group + 1) * self._k // 2):
                Node.connect(self._node_map[f"edge_{z(i)}"], self._node_map[f"agg_{z(j)}"], DEFAULT_CHANNEL)

        # Connect aggreagte to core
        core_counter = 0
        for i in range(self._k ** 2 // 2):
            for j in range(self._k // 2):
                Node.connect(self._node_map[f"agg_{z(i)}"], self._node_map[f"core_{z(core_counter)}"], DEFAULT_CHANNEL)
                core_counter = (core_counter + 1) % (self._k ** 2 // 4)
        
        # generate_random_flows(self, 10)

        return self

class Jellyfish(Network):
    def __init__(self, name, num_switches, ports_per_switch, internal_ports, package=PACKAGE, imports=IMPORTS, width=800, height=500):
        super().__init__(name, package, imports, width, height)
        assert ports_per_switch > internal_ports
        self._n = num_switches  # number of routers
        self._k = ports_per_switch  # number of ports per router
        self._r = internal_ports  # number of ports connecting to other routers
        assert(internal_ports >= 2)  # core needs to be connected
        self._servers = []
        self._clients = []

    def initialize(self):
        def z(num, n=2):
            return f"{num}".zfill(n)

        self._lines = [
            Line(DEFAULT_CHANNEL, DEFAULT_LINE_PARAMS), 
            Line(INFINITE_CHANNEL, INFINITE_LINE_PARAMS)
        ]

        for i in range(self._n):
            self._node_map[f"core_{z(i)}"] = Router(f"core_{z(i)}", 
                self._width / 2 + 150 * math.cos(2 * math.pi * i / self._n), 
                self._height / 2 + 150 * math.sin(2 * math.pi * i / self._n))

        num_hosts = self._n * (self._k - self._r)
        slide = 0 if self._k == self._r + 1  else 0.5
        for i in range(num_hosts):
            server_x = self._width / 2 + 200 * math.cos(2 * math.pi * (i - slide) / num_hosts)
            server_y = self._height / 2 + 200 * math.sin(2 * math.pi * (i - slide) / num_hosts)
            server_src_x = self._width / 2 + 250 * math.cos(2 * math.pi * (i - slide - 0.25) / num_hosts)
            server_src_y = self._height / 2 + 250 * math.sin(2 * math.pi * (i - slide - 0.25) / num_hosts)
            server_sink_x = self._width / 2 + 250 * math.cos(2 * math.pi * (i - slide + 0.25) / num_hosts)
            server_sink_y = self._height / 2 + 250 * math.sin(2 * math.pi * (i - slide + 0.25) / num_hosts)
            self._node_map[f"host_{z(i)}"] = Server(f"host_{z(i)}", 
                server_x, server_y, (server_src_x, server_src_y), (server_sink_x, server_sink_y))

        # make sure there is at least one cycle in the graph
        rands = [idx for idx in range(self._n)]
        random.shuffle(rands)
        for i in range(self._n):
            Node.connect(self._node_map[f"core_{z(rands[i])}"], self._node_map[f"core_{z(rands[(i + 1) % self._n])}"], DEFAULT_CHANNEL)

        for i in range(self._n):
            core_node = self._node_map[f"core_{z(i)}"]
            if (self._r == core_node.get_num_gates()):
                continue  # router is already fully connected
            potential_neighbors = [self._node_map[node_name] for node_name in self.get_categorized_host_names()['core']]
            potential_neighbors = [node for node in filter(lambda node: node.get_num_gates() < self._r, potential_neighbors)]
            potential_neighbors = [node for node in filter(lambda node: not core_node.is_connected_to(node), potential_neighbors)]

            neighbors = potential_neighbors
            if (self._r - core_node.get_num_gates() <= len(potential_neighbors)):
                neighbors = random.sample(potential_neighbors, self._r - core_node.get_num_gates())
            else:
                print(f"Not enough potential neighbors for node {i}")
            
            for neighbor in neighbors:
                Node.connect(core_node, neighbor, DEFAULT_CHANNEL)
        
        for i in range(num_hosts):
            host_node = self._node_map[f"host_{z(i)}"]
            router_node = self._node_map[f"core_{z(int(i / (self._k - self._r)))}"]
            Node.connect(host_node, router_node, DEFAULT_CHANNEL)

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

        self._lines = [
            Line(DEFAULT_CHANNEL, DEFAULT_LINE_PARAMS), 
            Line(INFINITE_CHANNEL, INFINITE_LINE_PARAMS)
        ]

        for i in range(self._a // 2):
            self._node_map[f"core_{z(i)}"] = Router(f"core_{z(i)}", 
                self._width * (i + 0.5) / (self._a // 2), 100)
        
        for i in range(self._c):
            self._node_map[f"agg_{z(i)}"] = Router(f"agg_{z(i)}",  
                self._width * (i + 0.5) / (self._c), 200)
        
        for i in range(self._a * self._c // 4):
            self._node_map[f"tor_{z(i)}"] = Tor(f"tor_{z(i)}", 
                self._width * (i + 0.5) / (self._a * self._c // 4), 300)

        for i in range(self._s * self._a * self._c // 4):
            self._node_map[f"host_{z(i)}"] = Server(f"host_{z(i)}", 
                self._width * (i + 0.5) / (self._s * self._a * self._c // 4), 400)

        # Connect hosts to tor routers
        tor_index = 0
        tor_counter = 0
        for i in range(self._s * self._a * self._c // 4):
            Node.connect(self._node_map[f"host_{z(i)}"], self._node_map[f"tor_{z(tor_index)}"], DEFAULT_CHANNEL)
            tor_counter += 1
            if tor_counter == self._s:
                tor_index += 1
                tor_counter = 0

        # Connect tor to aggregate
        for i in range(self._a * self._c // 4):
            group = i // (self._a // 2)
            for j in range(group * 2, (group + 1) * 2):
                Node.connect(self._node_map[f"tor_{z(i)}"], self._node_map[f"agg_{z(j)}"], DEFAULT_CHANNEL)

        # Connect aggregate to core
        for i in range(self._c):
            for j in range(self._a // 2):
                Node.connect(self._node_map[f"agg_{z(i)}"], self._node_map[f"core_{z(j)}"], DEFAULT_CHANNEL)

        return self

flows = []
def generate_random_flows(clients, servers, n):
    if len(flows) == 0:
        for i in range(n):
            p = np.random.normal(4, 1)
            while p < 3:
                p = np.random.normal(4, 1)
            flows.append(10 ** p)
    
    for i, client in enumerate(clients):
        server = servers[(i + len(servers) // 2) % len(servers)]
        client.add_flow(server, 12500000, 0)  # 10 Mbit flow

    #for i in range(n):
    #    client = random.sample(clients, 1)[0]
    #    server = random.sample(servers, 1)[0]
    #    # client.add_flow(server, flows[i], 0)
    #    client.add_flow(server, 1250000, 0)  # 1 Mbit flow

def main():
    random.seed(0)
    np.random.seed(0)

    network = Network(name="Default", use_visualizer=True).initialize()
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")


    network = FatTree(name="FatTree", switch_degree=4).initialize()
    def z(num, n=2):
        return f"{num}".zfill(n)
    for i in range(8):
        src = f"host_{z(i)}"
        dest = f"host_{z((i + 8) % 16)}"
        network.add_flow(src, dest, 1000000, 0)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")

    network = Jellyfish(name="Jelly", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    for i in range(8):
        src = f"host_{z(i)}"
        dest = f"host_{z((i + 8) % 16)}"
        network.add_flow(src, dest, 1000000, 0)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")

    network = VL2(name="VL2", ports_per_core_switch=4, ports_per_aggregate_switch=4, hosts_per_tor=4).initialize()
    for i in range(8):
        src = f"host_{z(i)}"
        dest = f"host_{z((i + 8) % 16)}"
        network.add_flow(src, dest, 1000000, 0)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")
    return

if __name__ == "__main__":
    main()