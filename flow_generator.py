from constants import *
import math, random, copy

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

class FlowGenerator:
    @staticmethod
    def add_k_random_flows(network, k, flow_size):
        hosts = network.get_categorized_nodes()['host']
        for _ in range(k):
            src, dest = random.sample(hosts, 2)
            network.add_flow(src, dest, flow_size, 0)
        return

    @staticmethod
    def add_random_paired_flows(network, flow_size):
        hosts = network.get_categorized_nodes()['host']
        if len(hosts) % 2 != 0:
            print(f"Cannot add paired flows with odd number of hosts [{len(hosts)}]")
        indices = [i for i in range(len(hosts))]
        for _ in range(len(hosts) // 2):
            src_idx, dest_idx = random.sample(indices, 2)
            src = hosts[src_idx]
            dest = hosts[dest_idx]
            network.add_flow(src, dest, flow_size, 0)
            indices.remove(src_idx)
            indices.remove(dest_idx)
        return