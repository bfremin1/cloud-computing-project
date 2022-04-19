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

PLT_SAVE_FIGS = False
PLT_SHOW_FIGS = True

TREE_K = [4, 12] # [4, 12]

JELLY_TRIALS = 10 # 10
JELLY_SWITCHES = [8, 12] # [4, 25]
JELLY_PORTS = [5, 8] # [3, 15]
JELLY_K = [4, 10] # [1, 10]

VL_CORE = [2, 10] # [2, 10]
VL_AGG = [2, 10] # [2, 10]

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
        plt.savefig("graphs/" + title + ".png")
    if PLT_SHOW_FIGS:
        plt.show()
    else:
        plt.clf()

"""
Generate FatTree path length graphs for each parameter k
"""
def gen_dist_tree(K):
    for k in range(K[0], K[1] + 1, 2):
        network = FatTree(name="FatTree_" + str(k), switch_degree=k).initialize()
        hosts = network.get_categorized_nodes()['host']
        netx = RoutingAlgorithm.get_nx_graph(network)
        path_lengths = []
        for i in range(len(hosts)):
            for j in range(i + 1, len(hosts)):
                path_lengths.append(
                    len(RoutingAlgorithm.single_shortest_path(netx,
                                                              hosts[i].get_name(),
                                                              hosts[j].get_name()
                    )) - 1
                )
                
        plt_hist(data = path_lengths,
                 title = "Path length distribution for " + network.get_name(),
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

"""
Generate Jellyfish average path length graphs for each amount of
switches, ports, and internal ports over k shortest paths for each k
"""
def gen_dist_jelly(SWITCHES, PORTS, K, TRIALS):
    for switches in range(SWITCHES[0], SWITCHES[1] + 1):
        for ports in range(PORTS[0], PORTS[1] + 1):
            for internals in range(3, min(ports, switches // 2 + 1)):
                for trial in range(TRIALS):
                    path_lengths_dict = {}
                    network = Jellyfish(name="Jelly_"
                                        + str(switches) + "_"
                                        + str(ports) + "_"
                                        + str(internals) + "-"
                                        + str(trial),
                                        num_switches=switches,
                                        ports_per_switch=ports,
                                        internal_ports=internals).initialize()
                    hosts = network.get_categorized_nodes()['host']
                    netx = RoutingAlgorithm.get_nx_graph(network)
                    for k in range(K[0], K[1] + 1):
                        if k not in path_lengths_dict.keys():
                            path_lengths_dict[k] = []
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
                             title = "Average path length distribution for Jellyfish_"
                             + str(switches) + "_"
                             + str(ports) + "_"
                             + str(internals)
                             + " over " + str(k) + " shortest paths, "
                             + str(JELLY_TRIALS) + " trials",
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
                    
"""
Generate VL2 path length graphs for each amount of core and aggregate ports
"""
def gen_dist_vl(CORE, AGG):
    for core_ports in range(CORE[0], CORE[1] + 1, 2):
        for aggregate_ports in range(AGG[0], AGG[1] + 1, 2):
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
                        len(RoutingAlgorithm.single_shortest_path(netx,
                                                                  hosts[i].get_name(),
                                                                  hosts[j].get_name()
                        )) - 1
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

def main():
    # Fix randomness for reproducability
    random.seed(0)
    np.random.seed(0)
    gen_dist_tree(TREE_K)

    random.seed(0)
    np.random.seed(0)
    gen_dist_jelly(JELLY_SWITCHES, JELLY_PORTS, JELLY_K, JELLY_TRIALS)

    random.seed(0)
    np.random.seed(0)
    gen_dist_vl(VL_CORE, VL_AGG)

if __name__ == "__main__":
    main()
        
            
