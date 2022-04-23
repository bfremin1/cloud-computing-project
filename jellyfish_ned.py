from network_ned import *
import math, random

class Jellyfish(Network):
    def __init__(self, name, num_switches, ports_per_switch, internal_ports, **kwargs):
        super().__init__(name, **kwargs)
        assert ports_per_switch > internal_ports
        self._n = num_switches  # number of routers
        self._k = ports_per_switch  # number of ports per router
        self._r = internal_ports  # number of ports connecting to other routers
        assert(internal_ports >= 2)  # core needs to be connected
        self._servers = []
        self._clients = []

    def initialize(self):
        self._lines = [
            Line(DEFAULT_CHANNEL, DEFAULT_LINE_PARAMS), 
            Line(INFINITE_CHANNEL, INFINITE_LINE_PARAMS)
        ]

        for i in range(self._n):
            self._node_map[f"core_{zfill(i)}"] = Router(f"core_{zfill(i)}", 
                self._width / 2 + 125 * math.cos(2 * math.pi * i / self._n), 
                self._height / 2 + 125 * math.sin(2 * math.pi * i / self._n))

        num_hosts = self._n * (self._k - self._r)
        slide = 0 if self._k == self._r + 1  else 0.5
        for i in range(num_hosts):
            server_x = self._width / 2 + 200 * math.cos(2 * math.pi * (i - slide) / num_hosts)
            server_y = self._height / 2 + 200 * math.sin(2 * math.pi * (i - slide) / num_hosts)
            server_src_x = self._width / 2 + 250 * math.cos(2 * math.pi * (i - slide - 0.25) / num_hosts)
            server_src_y = self._height / 2 + 250 * math.sin(2 * math.pi * (i - slide - 0.25) / num_hosts)
            server_sink_x = self._width / 2 + 250 * math.cos(2 * math.pi * (i - slide + 0.25) / num_hosts)
            server_sink_y = self._height / 2 + 250 * math.sin(2 * math.pi * (i - slide + 0.25) / num_hosts)
            self._node_map[f"host_{zfill(i)}"] = Server(f"host_{zfill(i)}", 
                server_x, server_y, (server_src_x, server_src_y), (server_sink_x, server_sink_y))

        # make sure there is at least one cycle in the graph
        rands = [idx for idx in range(self._n)]
        random.shuffle(rands)
        for i in range(self._n):
            Node.connect(self._node_map[f"core_{zfill(rands[i])}"], self._node_map[f"core_{zfill(rands[(i + 1) % self._n])}"], DEFAULT_CHANNEL)

        for i in range(self._n):
            core_node = self._node_map[f"core_{zfill(i)}"]
            if (self._r == core_node.get_num_gates()):
                continue  # router is already fully connected
            potential_neighbors = self.get_categorized_nodes()['core']
            potential_neighbors = [node for node in filter(lambda node: node.get_num_gates() < self._r, potential_neighbors)]
            potential_neighbors = [node for node in filter(lambda node: not core_node.is_connected_to(node), potential_neighbors)]

            neighbors = potential_neighbors
            if (self._r - core_node.get_num_gates() <= len(potential_neighbors)):
                neighbors = random.sample(potential_neighbors, self._r - core_node.get_num_gates())
            else:
                print(f"Not enough potential neighbors for node {i} [ looking={self._r - core_node.get_num_gates()} neighbors={len(potential_neighbors)} ]")
            
            for neighbor in neighbors:
                Node.connect(core_node, neighbor, DEFAULT_CHANNEL)
        
        for i in range(num_hosts):
            host_node = self._node_map[f"host_{zfill(i)}"]
            router_node = self._node_map[f"core_{zfill(int(i / (self._k - self._r)))}"]
            Node.connect(host_node, router_node, DEFAULT_CHANNEL)

        return self
    
    def add_n_fully_connected_core_routers(self, n, k):
        if k % 2 != 0 or n == 0:
            print(f"k={k} n={n} --- Cannot add using Jellyfish protocol")
            return

        first_index = len(self.get_categorized_nodes()['core'])
        for i in range(n):
            router_name = f"core_{zfill(first_index + i)}"
            self._node_map[router_name] = Router(router_name,
                self._width / 2 + 50 * math.cos(2 * math.pi * i / n), 
                self._height / 2 + 50 * math.sin(2 * math.pi * i / n)
            )
            for _ in range(k // 2):
                graph = RoutingAlgorithm.get_nx_graph(self)
                neighbors = list(graph.neighbors(router_name))
                neighbors.append(router_name)
                def connectable(edge):
                    return edge[0] not in neighbors and edge[1] not in neighbors and 'core' in edge[0] and 'core' in edge[1]
                edges = [e for e in filter(connectable, graph.edges())]
                if len(edges) == 0:
                    print("No edges to select from :/")
                    break
                rand_edge = random.sample(edges, 1)[0]
                Node.disconnect(self._node_map[rand_edge[0]], self._node_map[rand_edge[1]])
                Node.connect(self._node_map[router_name], self._node_map[rand_edge[0]])
                Node.connect(self._node_map[router_name], self._node_map[rand_edge[1]])

        return self