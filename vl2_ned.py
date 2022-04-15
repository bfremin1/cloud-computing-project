from network_ned import *

class VL2(Network):
    def __init__(self, name, ports_per_core_switch, ports_per_aggregate_switch, hosts_per_tor, **kwargs):
        super().__init__(name, **kwargs)
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