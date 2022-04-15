from constants import *
from basic_ned import Connection, Configurator, Visualizer, Line
from nodes_ned import Node, Router, Server, Tor, Source, Sink
from routing_algorithms import RoutingAlgorithm

class Network:
    def __init__(self, name, package=None, imports=IMPORTS, width=1200, height=500, use_visualizer=False):
        if package is None:
            package = get_package_name()
        self._name = name
        self._package = package
        self._imports = imports
        self._width = int(width)
        self._height = int(height)
        self._node_map = {}
        self._configurator = Configurator(50, 50)
        self._visualizer = Visualizer(50, 100) if use_visualizer else None
        self._flow_counter = 0
        self._lines = []
        self._flows = []
        self._categorized_nodes = None
    
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

        return self

    def get_categorized_nodes(self):
        if self._categorized_nodes:
            return self._categorized_nodes
        self._categorized_nodes = {}
        # Add all node names to map
        for node_name in self._node_map.keys():
            node_type = node_name.split("_")[0]
            if node_type not in self._categorized_nodes:
                self._categorized_nodes[node_type] = []
            self._categorized_nodes[node_type].append(node_name)
        # sort node names within category
        for node_type in self._categorized_nodes.keys():
            self._categorized_nodes[node_type] = sorted(self._categorized_nodes[node_type])
        # covnert node names to actual nodes
        for node_type in self._categorized_nodes.keys():
            self._categorized_nodes[node_type] = [self._node_map[node_name] for node_name in self._categorized_nodes[node_type]]
        return self._categorized_nodes

    def add_flow(self, send, recv, amount, start):
        if isinstance(send, str):
            send = self._node_map[send]
        if isinstance(recv, str):
            recv = self._node_map[recv]
        source_name = f"source_{self._flow_counter}"
        sink_name = f"sink_{self._flow_counter}"
        self._flow_counter += 1
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

        fd = open(f"{get_working_directory()}/{self._name}.ned", "w")
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

        fd = open(f"{get_working_directory()}/{self._name}.ini", "w")
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
        fd = open(f"{get_working_directory()}/{self._name}.xml", "w")
        fd.write(xml_str)
        fd.close()

        return xml_str