from constants import *
from basic_ned import Connection
from flow import Flow

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