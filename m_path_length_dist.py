import random, sys, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import networkx as nx
import math

from constants import *
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from vl2_ned import VL2
from flow_generator import FlowGenerator
from routing_algorithms import RoutingAlgorithm

PLT_SAVE_FIG = True
PLT_SHOW_FIG = False

TREE_K_RANGE = [4, 14] # [4, 12]

JELLY_TRIALS = 10 # 10
JELLY_SWITCH_RANGE = [4, 24] # [4, 25]
JELLY_PORT_RANGE = [4, 16] # [3, 15]
JELLY_PATH_RANGE = [1, 10] # [1, 10]

VL_CORE_RANGE = [2, 10] # [2, 10]
VL_AGG_RANGE = [2, 10] # [2, 10]

STORAGE_DIR = "paths/"

def plt_hist_prop(data, label='', alpha=1.0):
    plt.hist(data, label=label, bins=np.arange(0, 12.25, 0.25), alpha=alpha, weights=np.ones_like(data) / len(data))

def plt_output(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(np.arange(0, 12.25, 0.25),
               [int(x / 4) if x % 4 == 0 else "" for x in np.arange(0, 49, 1)])
    plt.yticks([round(x, 1) for x in np.arange(0, 1.1, 0.1)],
               [round(x, 1) for x in np.arange(0, 1.1, 0.1)])
    plt.legend()
    if PLT_SAVE_FIG:
        plt.savefig(STORAGE_DIR + title.replace(' ', '-').replace('\n', '_') + ".png")
        plt.clf()
    if PLT_SHOW_FIG:
        plt.show()

def gen_dist_tree(k):
    network = FatTree(name="FatTree_" + str(k), switch_degree=k).initialize()
    hosts = network.get_categorized_nodes()['host']
    netx = RoutingAlgorithm.get_nx_graph(network)
    path_lengths = []
    for i in range(len(hosts)):
        for j in range(i + 1, len(hosts)):
            path_lengths.append(
                len(RoutingAlgorithm.k_shortest_paths(netx,
                                                      hosts[i].get_name(),
                                                      hosts[j].get_name(),
                                                      1
                )[0]) - 1
            )

    label = network.get_name()
    return (label, path_lengths)
    
def gen_dist_jelly(switches, ports, internals, cores, core_ports, path_range, trials, path_func):
    path_lengths_dict = {}
    for k in range(path_range[0], path_range[1] + 1):
        if k not in path_lengths_dict.keys() and path_func(k):
            path_lengths_dict[k] = []
            
    for trial in range(trials):
        network = Jellyfish(name="Jelly_"
                            + str(switches) + "_"
                            + str(ports) + "_"
                            + str(internals) + "-"
                            + str(trial),
                            num_switches=switches,
                            ports_per_switch=ports,
                            internal_ports=internals).initialize()
        network.add_n_fully_connected_core_routers(cores, core_ports)
        hosts = network.get_categorized_nodes()['host']
        netx = RoutingAlgorithm.get_nx_graph(network)
        for k in path_lengths_dict.keys():
            path_lengths = []
            for i in range(len(hosts)):
                for j in range(i + 1, len(hosts)):
                    paths = RoutingAlgorithm.k_shortest_paths(netx,
                                                              hosts[i].get_name(),
                                                              hosts[j].get_name(),
                                                              k)
                    lengths = list(map(lambda path: len(path) - 1, paths))
                    path_lengths.append(np.mean(lengths))
            path_lengths_dict[k].extend(path_lengths)
    graphs = []
    for k in path_lengths_dict.keys():
        label = "Jellyfish_" + str(switches * (ports - internals)) + "_" + str(switches + cores) + "_" + str(ports - internals) + "-" + str(k)
        graphs.append((label, path_lengths_dict[k]))
    return graphs
            
def gen_dist_vl(core_ports, aggregate_ports):
    network = VL2(name="VL2_"
                  + str(core_ports) + "_"
                  + str(aggregate_ports),
                  ports_per_core_switch=core_ports,
                  ports_per_aggregate_switch=aggregate_ports,
                  hosts_per_tor=10).initialize()
    hosts = network.get_categorized_nodes()['host']
    netx = RoutingAlgorithm.get_nx_graph(network)
    path_lengths = []
    for i in range(len(hosts)):
        for j in range(i + 1, len(hosts)):
            path_lengths.append(
                len(RoutingAlgorithm.k_shortest_paths(netx,
                                                      hosts[i].get_name(),
                                                      hosts[j].get_name(),
                                                      1
                )[0]) - 1
            )
    label = network.get_name()
    return (label, path_lengths)
            
def gen_dist_tree_range(k_range):
    graphs = []
    for k in range(k_range[0], k_range[1] + 1, 2):
        graphs.append(gen_dist_tree(k))

def gen_dist_jelly_range(switch_range, port_range, path_range, trials, path_func):
    graphs = []
    for switches in range(switch_range[0], switch_range[1] + 1):
        for ports in range(port_range[0], port_range[1] + 1):
            for internals in range(3, min(ports, switches // 2 + 1)):
                graphs.append(gen_dist_jelly(switches, ports, internals, 0, 0, path_range, trials, path_func))
                    
def gen_dist_vl_range(core_range, agg_range):
    graphs = []
    for core in range(core_range[0], core_range[1] + 1, 2):
        for agg in range(agg_range[0], agg_range[1] + 1, 2):
            graphs.append(gen_dist_vl(core, agg))

def gen_dist_jelly_treelike_full_first(k, path_range, trials, path_func):
    hosts = (k ** 3) // 4
    nodes = 5 * (k ** 2) // 4
    for cluster_size in range(1, k - 1):
        if hosts % cluster_size == 0:
            switches = hosts // cluster_size
            if switches <= nodes:
                return gen_dist_jelly(switches, k, k - cluster_size, nodes - switches, k, path_range, trials, path_func)

def gen_dist_jelly_treelike_nodes(k, path_range, trials, path_func):
    nodes = 5 * (k ** 2) // 4
    return gen_dist_jelly(nodes, k, k - 1, 0, 0, path_range, trials, path_func)

def gen_dist_jelly_treelike_hosts(k, path_range, trials, path_func):
    hosts = (k ** 3) // 4
    return gen_dist_jelly(hosts, k, k - 1, 0, 0, path_range, trials, path_func)

def gen_dist_jelly_range_treelike_full(k_range, path_range, trials, path_func):
    graphs = []
    for k in range(k_range[0], k_range[1] + 1, 2):
        graphs.append(gen_dist_jelly_treelike_full(k, path_range, trials, path_func))
    return graphs

def gen_dist_jelly_range_treelike_nodes(k_range, path_range, trials):
    graphs = []
    for k in range(k_range[0], k_range[1] + 1, 2):
        graphs.append(gen_dist_jelly_treelike_nodes(k, path_range, trials, path_func))
    return graphs

def gen_dist_jelly_range_treelike_hosts(k_range, path_range, trials, path_func):
    graphs = []
    for k in range(k_range[0], k_range[1] + 1, 2):
        graphs.append(gen_dist_jelly_treelike_hosts(k, path_range, trials, path_func))
    return graphs

def gen_essentials():

    print(f"Comparing FatTree with similar Jellyfish(es), k={TREE_K_RANGE[0]:d} to k={TREE_K_RANGE[1]:d}")
    
    # Fix randomness for reproducability
    random.seed(0)
    np.random.seed(0)

    p_set = [1, 2, 4, 8]

    for k in range(TREE_K_RANGE[0], TREE_K_RANGE[1] + 1, 2):

        print(f"Generating plots for k = {k:d}...")
        
        tree = gen_dist_tree(k)
        jellies = gen_dist_jelly_treelike_full_first(k, JELLY_PATH_RANGE, JELLY_TRIALS, lambda x: x in p_set)

        if k < 8:
            jelly_hosts = gen_dist_jelly_treelike_hosts(k, JELLY_PATH_RANGE, JELLY_TRIALS, lambda x: x in p_set)
            jelly_nodes = gen_dist_jelly_treelike_nodes(k, JELLY_PATH_RANGE, JELLY_TRIALS, lambda x: x in p_set)

        for i in range(len(jellies)):
            p = p_set[i]
            plt_hist_prop(tree[1], tree[0], alpha=0.5)
            plt_hist_prop(jellies[i][1], jellies[i][0], alpha=0.5)
            plt_output("FatTree (k=" + str(k) + ") vs. Equivalent Jellyfish (p=" + str(p) + "), " + str(JELLY_TRIALS) + " trials",
                       "Average Path Length", "Relative Frequency")
            if k < 8:
                plt_hist_prop(tree[1], tree[0], alpha=0.5)
                plt_hist_prop(jelly_hosts[i][1], jelly_hosts[i][0], alpha=0.5)
                plt_output("FatTree (k=" + str(k) + ") vs. Equivalent Jellyfish Hosts (p=" + str(p) + "), " + str(JELLY_TRIALS) + " trials",
                           "Average Path Length", "Relative Frequency")
                plt_hist_prop(tree[1], tree[0], alpha=0.5)
                plt_hist_prop(jelly_nodes[i][1], jelly_nodes[i][0], alpha=0.5)
                plt_output("FatTree (k=" + str(k) + ") vs. Equivalent Jellyfish Internals (p=" + str(p) + "), " + str(JELLY_TRIALS) + " trials",
                           "Average Path Length", "Relative Frequency")
    
def main():
    global STORAGE_DIR
    if len(sys.argv) > 1:
        STORAGE_DIR = sys.argv[1]
    if STORAGE_DIR[-1] != '/':
        STORAGE_DIR = STORAGE_DIR + '/'
    os.makedirs(STORAGE_DIR, exist_ok=True)
    gen_essentials()

if __name__ == "__main__":
    main()
    
            
