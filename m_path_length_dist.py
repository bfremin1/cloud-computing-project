import random, sys
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math

from constants import *
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from vl2_ned import VL2
from flow_generator import FlowGenerator
from routing_algorithms import RoutingAlgorithm

PLT_SAVE_FIGS = True
PLT_SHOW_FIGS = False

TREE_K_RANGE = [4, 12] # [4, 12]

JELLY_TRIALS = 10 # 10
JELLY_SWITCH_RANGE = [4, 24] # [4, 25]
JELLY_PORT_RANGE = [4, 16] # [3, 15]
JELLY_K_RANGE = [4, 10] # [1, 10]

VL_CORE_RANGE = [2, 10] # [2, 10]
VL_AGG_RANGE = [2, 10] # [2, 10]

def plt_hist(data, title='', xlabel='', ylabel='', bins=[], xticks=[], yticks=[]):
    bin_strat = 'auto' if (len(bins) == 0) else bins
    plt.hist(data, bins=bin_strat)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xticks:
        plt.xticks(xticks[0], xticks[1])
    if yticks:
        plt.yticks(yticks[0], yticks[1])
    if PLT_SAVE_FIGS:
        plt.savefig("graphs/" + title.replace(' ', '-').replace('\n', '_') + ".png")
    if PLT_SHOW_FIGS:
        plt.show()
    else:
        plt.clf()

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
            
    plt_hist(data = path_lengths,
             title = "Path length for FatTree\n" + "(k=" + str(k) + ")",
             xlabel = "Path length",
             ylabel = "Frequency",
             bins = np.arange(np.min(path_lengths), np.max(path_lengths) + 2),
             xticks = [
                 np.arange(0.5, np.max(path_lengths) + 1.51, 1),
                 np.arange(0, np.max(path_lengths) + 1.01, 1)
             ],
             yticks = [
                 np.arange(0, len(path_lengths),
                           10 ** math.floor(math.log10(len(path_lengths)))),
                 np.arange(0, len(path_lengths),
                           10 ** math.floor(math.log10(len(path_lengths))))
             ]
    )
    
def gen_dist_jelly(switches, ports, internals, cores, core_ports, path_range, trials):
    path_lengths_dict = {}
    for k in range(path_range[0], path_range[1] + 1):
        if k not in path_lengths_dict.keys():
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
        for k in range(path_range[0], path_range[1] + 1):
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
                        
    for k in path_lengths_dict.keys():
        plt_hist(data = path_lengths_dict[k],
                 title = "Average path length for Jellyfish\n"
                 + "(hosts=" + str(switches * (ports - internals)) + ", "
                 + "switches=" + str(switches + cores) + ", "
                 + "cluster=" + str(ports - internals) + ")\n"
                 + "over " + str(k) + " shortest paths, "
                 + str(trials) + " trials",
                 xlabel = "Average path length",
                 ylabel = "Frequency",
                 bins = np.arange(0, np.max(path_lengths_dict[k]) + 1 / k, 1 / k),
                 xticks = [
                     np.arange(0.5 / k, np.max(path_lengths) + 1.5 / k + 0.01, 1 / k),
                     [round(i) if i % 1 < 0.01 or i % 1 > 0.99 else ''
                      for i in np.arange(0, np.max(path_lengths) + 1 / k + 0.01, 1 / k)]
                 ],
                 yticks = [
                     np.arange(0, len(path_lengths),
                               10 ** math.floor(math.log10(len(path_lengths)))),
                     np.arange(0, len(path_lengths),
                               10 ** math.floor(math.log10(len(path_lengths))))
                 ]
        )
            
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
            
    plt_hist(data = path_lengths,
             title = "Path length distribution for " + network.get_name(),
             xlabel = "Path length",
             ylabel = "Frequency",
             bins = np.arange(np.min(path_lengths), np.max(path_lengths) + 2),
             xticks = [
                 np.arange(0.5, np.max(path_lengths) + 1.5, 1),
                 np.arange(0, np.max(path_lengths) + 1, 1)
             ],
             yticks = [
                 np.arange(0, len(path_lengths),
                           10 ** math.floor(math.log10(len(path_lengths)))),
                 np.arange(0, len(path_lengths),
                           10 ** math.floor(math.log10(len(path_lengths))))
             ]
    )
            
"""
Generate FatTree path length graphs for each parameter k
"""
def gen_dist_tree_range(k_range):
    for k in range(k_range[0], k_range[1] + 1, 2):
        gen_dist_tree(k)

"""
Generate Jellyfish average path length graphs for each amount of
switches, ports, and internal ports over k shortest paths for each k
"""
def gen_dist_jelly_range(switch_range, port_range, path_range, trials):
    for switches in range(switch_range[0], switch_range[1] + 1):
        for ports in range(port_range[0], port_range[1] + 1):
            for internals in range(3, min(ports, switches // 2 + 1)):
                gen_dist_jelly(switches, ports, internals, 0, 0, path_range, trials)
                    
"""
Generate VL2 path length graphs for each amount of core and aggregate ports
"""
def gen_dist_vl_range(core_range, agg_range):
    for core in range(core_range[0], core_range[1] + 1, 2):
        for agg in range(agg_range[0], agg_range[1] + 1, 2):
            gen_dist_vl(core, agg)

def gen_dist_jelly_range_treelike_full(k_range, path_range, trials):
    for k in range(k_range[0], k_range[1] + 1, 2):
        hosts = (k ** 3) // 4
        nodes = 5 * (k ** 2) // 4
        for cluster_size in range(1, k - 1):
            if hosts % cluster_size == 0:
                switches = hosts // cluster_size
                gen_dist_jelly(switches, k, k - cluster_size, nodes - switches, k, path_range, trials)

def gen_dist_jelly_range_treelike_nodes(k_range, path_range, trials):
    for k in range(k_range[0], k_range[1] + 1, 2):
        nodes = 5 * (k ** 2) // 4
        gen_dist_jelly(nodes, k, k - 1, 0, 0, path_range, trials)

def gen_dist_jelly__range_treelike_hosts(k_range, path_range, trials):
    for k in range(k_range[0], k_range[1] + 1, 2):
        hosts = (k ** 3) // 4
        gen_dist_jelly(hosts, k, k - 1, 0, 0, path_range, trials)

def main():
    # Fix randomness for reproducability
    random.seed(0)
    np.random.seed(0)
    gen_dist_tree_range(TREE_K_RANGE)

    # Fix randomness for reproducability
    random.seed(0)
    np.random.seed(0)
    gen_dist_jelly_range_treelike_full(TREE_K_RANGE, JELLY_K_RANGE, JELLY_TRIALS)

if __name__ == "__main__":
    main()
    
            
