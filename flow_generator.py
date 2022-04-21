from constants import *
import math, random
import numpy as np

class Flow:
    def __init__(self, src, dest, send_amount, start_delay):
        assert (send_amount > 0)
        self._src = src
        self._dest = dest
        self._send_amount = send_amount
        self._num_packets = math.ceil(send_amount/REQUEST_SIZE)
        self._start_delay = int(start_delay)
        self._path = None
    
    def cfg_str(self, network_name):
        return (f"module={network_name}.{self._src}.app[0] src={self._src} dest={self._dest}" + 
                f" num_bytes={self._send_amount} start_delay={self._start_delay} simtime={SIMULATION_TIME}")
    
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
            network.add_flow(src, dest, flow_size, 5)
        return

    @staticmethod
    def add_single_random_paired_flow(network, flow_size):
        hosts = network.get_categorized_nodes()['host']
        if len(hosts) % 2 != 0:
            print(f"Cannot add paired flows with odd number of hosts [{len(hosts)}]")
        indices = [i for i in range(len(hosts))]
        for _ in range(len(hosts) // 2):
            src_idx, dest_idx = random.sample(indices, 2)
            src = hosts[src_idx]
            dest = hosts[dest_idx]
            network.add_flow(src, dest, flow_size, 5)
            indices.remove(src_idx)
            indices.remove(dest_idx)
        return
    
    @staticmethod
    def add_random_paired_flows(network, total_flow, flow_size):
        assert flow_size >= 1000
        hosts = network.get_categorized_nodes()['host']
        if len(hosts) % 2 != 0:
            print(f"Cannot add paired flows with odd number of hosts [{len(hosts)}]")
        indices = [i for i in range(len(hosts))]
        for _ in range(len(hosts) // 2):
            src_idx, dest_idx = random.sample(indices, 2)
            src = hosts[src_idx]
            dest = hosts[dest_idx]
            flow_to_send = total_flow
            while (flow_to_send > 0):
                num_bytes = flow_size if flow_to_send > flow_size else flow_to_send
                network.add_flow(src, dest, num_bytes, 5)
                flow_to_send -= flow_size
            indices.remove(src_idx)
            indices.remove(dest_idx)
        return
    
    @staticmethod
    def add_random_paired_normal_flows(network, total_flow):
        hosts = network.get_categorized_nodes()['host']
        if len(hosts) % 2 != 0:
            print(f"Cannot add paired flows with odd number of hosts [{len(hosts)}]")
        indices = [i for i in range(len(hosts))]
        for _ in range(len(hosts) // 2):
            src_idx, dest_idx = random.sample(indices, 2)
            src = hosts[src_idx]
            dest = hosts[dest_idx]
            flow_to_send = total_flow
            counter = 0
            while (flow_to_send > 0):
                flow_size = FlowGenerator.flow_size_sample()
                num_bytes = flow_size if flow_to_send > flow_size else flow_to_send
                network.add_flow(src, dest, num_bytes, 5)
                flow_to_send -= flow_size
                counter += 1
            print(f"Num flows added {counter}")
            indices.remove(src_idx)
            indices.remove(dest_idx)

        return
    
    @staticmethod
    def flow_size_sample():
        p = np.random.normal(4, 1)
        while p < 3:
            p = np.random.normal(4, 1)
        return 10 ** p
    
    @staticmethod
    def add_k_normal_random_flows(network, k):
        hosts = network.get_categorized_nodes()['host']
        for _ in range(k):
            p = np.random.normal(4, 1)
            while p < 3:
                p = np.random.normal(4, 1)
            flow_size = 10 ** p
            src, dest = random.sample(hosts, 2)
            network.add_flow(src, dest, flow_size, 5)
        return