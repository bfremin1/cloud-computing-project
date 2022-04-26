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

NUM_SEEDS = 10

class FileWriter:
    def __init__(self, function_name, topologies_file):
        self._topologies_file = topologies_file
        analysis_topology_dir = f"{get_working_directory()}/analysis/{function_name}"
        if not os.path.exists(analysis_topology_dir):
            os.makedirs(analysis_topology_dir)
        self._analysis_topologies_file = open(f"{analysis_topology_dir}/topologies.txt", "w")
    
    def __del__(self):
        self._analysis_topologies_file.close()

    def write(self, string):
        self._topologies_file.write(string)
        self._analysis_topologies_file.write(string)    

def simple_test(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    root = f"Jellyfish__{sys._getframe().f_code.co_name}"
    network = Jellyfish(name=f"{root}", num_switches=8, ports_per_switch=4, internal_ports=3, seed=0).initialize()
    network.add_n_fully_connected_core_routers(4, 4)
    # FlowGenerator.add_random_paired_flows(network, 1 * MB, 1 * MB)
    FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
    network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
    file_writer.write(f"{network.get_name()} root={root}\n")

def fvj_flat_traffic_baseline(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    for seed in range(NUM_SEEDS):
        root = f"Jellyfish_16_4_3__{sys._getframe().f_code.co_name}"
        network = Jellyfish(name=f"{root}_seed{seed}_jitter", num_switches=16, ports_per_switch=4, internal_ports=3, seed=seed).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
        topologies_file.write(f"{network.get_name()} root={root}\n")
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"FatTree_4"
        network = FatTree(name=f"{root}_seed{seed}_jitter", switch_degree=4, seed=seed).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"VL2_8_8_1"
        network = VL2(name=f"{root}_seed{seed}_jitter", ports_per_core_switch=8, ports_per_aggregate_switch=8, hosts_per_tor=1, seed=seed).initialize()
        FlowGenerator.add_random_paired_flows(network, 1 * MB, 100 * KB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
        file_writer.write(f"{network.get_name()} root={root}\n")

def fvj_dc_traffic_baseline(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    for seed in range(NUM_SEEDS):
        root = f"Jellyfish_16_4_3__{sys._getframe().f_code.co_name}"
        network = Jellyfish(name=f"{root}_seed{seed}", num_switches=16, ports_per_switch=4, internal_ports=3, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"FatTree_4__{sys._getframe().f_code.co_name}"
        network = FatTree(name=f"{root}_seed{seed}", switch_degree=4, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"VL2_8_8_1__{sys._getframe().f_code.co_name}"
        network = VL2(name=f"{root}_seed{seed}", ports_per_core_switch=8, ports_per_aggregate_switch=8, hosts_per_tor=1, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
        file_writer.write(f"{network.get_name()} root={root}\n")

def fvj_el_traffic_baseline(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    for seed in range(NUM_SEEDS):
        root = f"Jellyfish_16_4_3__{sys._getframe().f_code.co_name}"
        network = Jellyfish(name=f"{root}_seed{seed}_jitter", num_switches=16, ports_per_switch=4, internal_ports=3, seed=seed).initialize()
        FlowGenerator.add_random_paired_mice_elephant_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"FatTree_4__{sys._getframe().f_code.co_name}"
        network = FatTree(name=f"{root}_seed{seed}_jitter", switch_degree=4, seed=seed).initialize()
        FlowGenerator.add_random_paired_mice_elephant_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"VL2_8_8_1__{sys._getframe().f_code.co_name}"
        network = VL2(name=f"{root}_seed{seed}_jitter", ports_per_core_switch=8, ports_per_aggregate_switch=8, hosts_per_tor=1, seed=seed).initialize()
        FlowGenerator.add_random_paired_mice_elephant_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
        file_writer.write(f"{network.get_name()} root={root}\n")

def fvj_dc_big_traffic(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    for seed in range(NUM_SEEDS):
        root = f"Jellyfish__{sys._getframe().f_code.co_name}"
        network = Jellyfish(name=f"{root}_seed{seed}", num_switches=27, ports_per_switch=6, internal_ports=4, seed=seed).initialize()
        network.add_n_fully_connected_core_routers(45 - 27, 6)  # same number of routers as FatTree
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"FatTree_6__{sys._getframe().f_code.co_name}"
        network = FatTree(name=f"{root}_seed{seed}", switch_degree=6, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.ECMP))
        file_writer.write(f"{network.get_name()} root={root}\n")

        root = f"VL2_6_18_1__{sys._getframe().f_code.co_name}"
        network = VL2(name=f"{root}_seed{seed}", ports_per_core_switch=6, ports_per_aggregate_switch=18, hosts_per_tor=1, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
        file_writer.write(f"{network.get_name()} root={root}\n")

def jelly_hosts_per_router(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    configs = [
        (24, 6, 5, 4),
        (12, 6, 4, 4),
        (8, 6, 3, 4),
        (6, 6, 2, 4)
    ]

    for seed in range(NUM_SEEDS):
        for cfg in configs:
            s, p, i, k = cfg
            root = f"Jellyfish_{s}_{p}_{i}_{k}__{sys._getframe().f_code.co_name}"
            network = Jellyfish(name=f"{root}_seed{seed}", num_switches=s, ports_per_switch=p, internal_ports=i, seed=seed).initialize()
            network.add_n_fully_connected_core_routers(24 - s, 6)
            FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
            network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=k))
            file_writer.write(f"{network.get_name()} seed={seed} root={root}\n")

def jv_k_4(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    # routers = da / 2 + dc
    # hosts = dc * da / 2 * hpt
    vl2_configs = [
        #(16, 4, 1),
        (8, 8, 1),
        # (4, 16, 1),
        (8, 4, 2),
        (4, 8, 2)#,
        #(4, 4, 4)
    ]

    for seed in range(NUM_SEEDS):
        for cfg in vl2_configs:
            dc, da, hpt = cfg
            root = f"VL2_{dc}_{da}_{hpt}__{sys._getframe().f_code.co_name}"
            network = VL2(name=f"{root}_seed{seed}", ports_per_core_switch=dc, ports_per_aggregate_switch=da, hosts_per_tor=hpt, seed=seed).initialize()
            FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
            network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.VLB))
            file_writer.write(f"{network.get_name()} seed={seed} root={root}\n")

        root = f"Jellyfish__{sys._getframe().f_code.co_name}"
        network = Jellyfish(name=f"{root}_seed{seed}", num_switches=16, ports_per_switch=4, internal_ports=3, seed=seed).initialize()
        FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
        network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=4))
        file_writer.write(f"{network.get_name()} root={root}\n")

def jelly_vary_num_switches(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    configs = [
        (8, 8, 7, 8),
        #(12, 8, 7, 4),
        (16, 8, 7, 8),
        #(20, 8, 7, 4),
        (24, 8, 7, 8),
        (32, 8, 7, 8)
    ]
    for seed in range(NUM_SEEDS):
        for cfg in configs:
            s, p, i, k = cfg
            root = f"Jellyfish_{s}_{p}_{i}_{k}__{sys._getframe().f_code.co_name}"
            network = Jellyfish(name=f"{root}_seed{seed}", num_switches=s, ports_per_switch=p, internal_ports=i, seed=seed).initialize()
            network.add_n_fully_connected_core_routers(24 - s, p)
            FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
            network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=k))
            file_writer.write(f"{network.get_name()} seed={seed} root={root}\n")

def jelly_extra_core_routers(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    config = (24, 4, 3, 4)
    total_num_routers = [24, 32, 40, 48]
    for seed in range(NUM_SEEDS):
        for n in total_num_routers:
            s, p, i, k = config
            root = f"Jellyfish_{s}_{p}_{i}_{k}_n{n}__{sys._getframe().f_code.co_name}"
            network = Jellyfish(name=f"{root}_seed{seed}", num_switches=s, ports_per_switch=p, internal_ports=i, seed=seed).initialize()
            network.add_n_fully_connected_core_routers(n - s, p)
            FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
            network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=k))
            file_writer.write(f"{network.get_name()} seed={seed} root={root}\n")

def jelly_faults(topologies_file):
    file_writer = FileWriter(sys._getframe().f_code.co_name, topologies_file)
    config = (24, 8, 7, 8)
    packet_error_proportion = [ '0.01', '0.001', '0.00001', '0' ]
    seed = 0
    for _ in range(NUM_SEEDS):
        for per in packet_error_proportion:
            s, p, i, k = config
            root = f"Jellyfish_{s}_{p}_{i}_{k}_per{per}__{sys._getframe().f_code.co_name}".replace("0.", "")
            network = Jellyfish(name=f"{root}_seed{seed}", num_switches=s, ports_per_switch=p, internal_ports=i, seed=seed).initialize()
            network._lines[0]._params['per'] = f"{per}"
            FlowGenerator.add_random_paired_normal_flows(network, 1 * MB)
            network.create_files(get_working_directory(), routing_algorithm(RoutingAlgorithm.KSP, k=k))
            file_writer.write(f"{network.get_name()} seed={seed} root={root}\n")
            seed += 1

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

    analysis_dir = f"{get_working_directory()}/analysis"
    if not os.path.exists(analysis_dir):
        os.makedirs(analysis_dir)
    
    topologies_file = open(f"{get_working_directory()}/topologies.txt", "w")
    simple_test(topologies_file)
    fvj_flat_traffic_baseline(topologies_file)
    fvj_dc_traffic_baseline(topologies_file)
    fvj_el_traffic_baseline(topologies_file)
    jelly_hosts_per_router(topologies_file)
    jelly_vary_num_switches(topologies_file)
    jelly_extra_core_routers(topologies_file)
    jelly_faults(topologies_file)
    jv_k_4(topologies_file)
    fvj_dc_big_traffic(topologies_file)
    topologies_file.close()
    return

if __name__ == "__main__":
    main()