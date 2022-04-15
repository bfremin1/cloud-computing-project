import random
import numpy as np

from constants import *
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from vl2_ned import VL2

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
    # Fix randomness for reproducability
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