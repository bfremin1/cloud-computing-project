from network_ned import *

class FatTree(Network):
    def __init__(self, name, switch_degree, **kwargs):
        super().__init__(name, **kwargs)
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