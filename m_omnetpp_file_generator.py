import random, sys, os
import numpy as np

from constants import *
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from routing_algorithms import RoutingAlgorithm, routing_algorithm
from vl2_ned import VL2
from flow_generator import FlowGenerator
import pickle as pkl

def all_three(topologies_file):
    for seed in range(4):
        random.seed(seed)
        np.random.seed(seed)
        network = FatTree(name=f"FatTree_{seed}", switch_degree=4).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        topologies_file.write(f"{network.get_name()} seed={seed} k=4\n")
        
        random.seed(seed)
        np.random.seed(seed)
        network = Jellyfish(name=f"Jellyfish_{seed}", num_switches=16, ports_per_switch=5, internal_ports=4).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm=routing_algorithm(RoutingAlgorithm.KSP, k=4))
        topologies_file.write(f"{network.get_name()} seed={seed} n=16 s=5 i=4 k=4\n")

        random.seed(seed)
        np.random.seed(seed)
        network = VL2(name=f"VL2_{seed}", ports_per_core_switch=4, ports_per_aggregate_switch=8, hosts_per_tor=2).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm=routing_algorithm(RoutingAlgorithm.VLB))
        topologies_file.write(f"{network.get_name()} seed={seed} dc=4 da=4 dpt=4\n")

def fat(topologies_file):
    for k in [2, 4, 6]:
        seed = 0
        random.seed(seed)
        np.random.seed(seed)
        network = FatTree(name=f"FatTree_{k}_{seed}", switch_degree=k).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        topologies_file.write(f"{network.get_name()} seed={seed} k={k}\n")

def jelly(topologies_file):
    configs = [
        (16, 4, 3, 4),
        (8, 8, 6, 4),
        (4, 16, 12, 4)
    ]

    seed = 0
    for cfg in configs:
        s, p, i, k = cfg
        root = f"Jellyfish_{s}_{p}_{i}_{k}"
        random.seed(seed)
        np.random.seed(seed)
        network = Jellyfish(name=f"{root}_{seed}", num_switches=s, ports_per_switch=p, internal_ports=i).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=k))
        topologies_file.write(f"{network.get_name()} seed={seed} root={root}\n")

def jelly_add(topologies_file):
    root = f"Jellyfish"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=8, ports_per_switch=4, internal_ports=3).initialize()
    network.add_n_fully_connected_core_routers(4, 4)
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 1 * MB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=2))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def test_brandon_1(topologies_file):
    root = f"Jellyfish_16_4_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"Jellyfish_16_4_3_fill"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    network.add_n_fully_connected_core_routers(4, 4)
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"FatTree_4"
    random.seed(0)
    np.random.seed(0)
    network = FatTree(name=f"{root}", switch_degree=4).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"VL2_8_8_1"
    random.seed(0)
    np.random.seed(0)
    network = VL2(name=f"{root}", ports_per_core_switch=8, ports_per_aggregate_switch=8, hosts_per_tor=1).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def test_brandon_2(topologies_file):
    root = f"Jellyfish_16_4_3_1pct"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    network._lines[0]._params['per'] = '0.001'
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_16_4_3_01pct"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    network._lines[0]._params['per'] = '0.0001'
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_16_4_3_001pct"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    network._lines[0]._params['per'] = '0.00001'
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def test_brandon_3(topologies_file):
    root = f"Jellyfish_4_4_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=4, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_8_4_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=8, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_12_4_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=12, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"Jellyfish_16_4_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    network._lines[0]._params['per'] = '0.001'
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def test_brandon_4(topologies_file):
    root = f"Jellyfish_12_6_5"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=12, ports_per_switch=6, internal_ports=5).initialize()
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_6_6_4"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=6, ports_per_switch=6, internal_ports=4).initialize()
    network.add_n_fully_connected_core_routers(6, 6)
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")
    
    root = f"Jellyfish_4_6_3"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=4, ports_per_switch=6, internal_ports=3).initialize()
    network.add_n_fully_connected_core_routers(8, 6)
    FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def test_brandon_5(topologies_file):
    root = f"FatTree_4"
    random.seed(0)
    np.random.seed(0)
    network = FatTree(name=f"{root}", switch_degree=4).initialize()
    FlowGenerator.add_random_paired_flows(network, 3 * MB, 300 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"Jellyfish_16_4_3_normal"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_normal_flows(network, 3 * MB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

    root = f"Jellyfish_16_4_3_flat"
    random.seed(0)
    np.random.seed(0)
    network = Jellyfish(name=f"{root}", num_switches=16, ports_per_switch=4, internal_ports=3).initialize()
    FlowGenerator.add_random_paired_flows(network, 3 * MB, 300 * KB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    topologies_file.write(f"{network.get_name()} root={root}\n")

def main():
    print(sys.argv)
    if (len(sys.argv) > 2):
        print("Usage: main.py [omnet_working_dir] [omnet_package_name]")
    if (len(sys.argv) >= 2):
        set_working_directory(sys.argv[1])    
    if (len(sys.argv) >= 3):
        set_package_name(sys.argv[2]) 
    print(f"Working directory set to: \'{get_working_directory()}\'")
    print(f"Package name set to: \'{get_package_name()}\'")

    topologies_file = open(f"{get_working_directory()}/topologies.txt", "w")
    test_brandon_5(topologies_file)
    topologies_file.close()
    return

if __name__ == "__main__":
    main()