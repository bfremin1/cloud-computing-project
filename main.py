import random, sys
import numpy as np

from constants import *
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from vl2_ned import VL2
from flow_generator import FlowGenerator

def main():
    if (len(sys.argv) > 2):
        print("Usage: main.py [omnet_working_dir]")
    if (len(sys.argv) == 2):
        set_working_directory(sys.argv[1])    
    print(f"Working directory set to: \'{WORKING_DIRECTORY}\'")

    topologies_file = open(f"{WORKING_DIRECTORY}/topologies.txt", "w")

    # Fix randomness for reproducability
    random.seed(0)
    np.random.seed(0)

    network = Network(name="Default", use_visualizer=True).initialize()
    FlowGenerator.add_k_random_flows(network, 3, 1000000)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")
    topologies_file.write(f"{network.get_name()}\n")

    network = FatTree(name="FatTree", switch_degree=4).initialize()
    FlowGenerator.add_random_paired_flows(network, 1000000)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")
    topologies_file.write(f"{network.get_name()}\n")

    network = Jellyfish(name="Jelly", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 1000000)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")
    topologies_file.write(f"{network.get_name()}\n")

    network = VL2(name="VL2", ports_per_core_switch=4, ports_per_aggregate_switch=4, hosts_per_tor=4).initialize()
    FlowGenerator.add_random_paired_flows(network, 1000000)
    ned_str = network.create_ned_file()
    ini_str = network.create_ini_file()
    xml_str = network.create_xml_file()
    print(f"{ned_str}\n{ini_str}\n{xml_str}\n")
    topologies_file.write(f"{network.get_name()}\n")

    topologies_file.close()
    return

if __name__ == "__main__":
    main()