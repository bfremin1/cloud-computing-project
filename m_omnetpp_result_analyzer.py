import random, sys, os
import numpy as np
import pandas as pd
import pickle as pkl
import matplotlib.pyplot as plt

from constants import *
from nodes_ned import Source
from network_ned import Network
from fattree_ned import FatTree
from jellyfish_ned import Jellyfish
from vl2_ned import VL2
from flow_generator import FlowGenerator

LINK_RATE = 1000
FATTREE_4_LATENCY = 1.8755624188311693

def main():
    show_plots = True
    if (len(sys.argv) > 2):
        print("Usage: main.py [omnet_working_dir]")
    if (len(sys.argv) >= 2):
        set_working_directory(sys.argv[1])    
    if (len(sys.argv) > 2):
        show_plots = False
    print(f"Working directory set to: \'{get_working_directory()}\'")

    if not os.path.exists(f"{get_working_directory()}/analysis"):
        print(f"ERROR: No analysis directory at: {get_working_directory()}/analysis")

    for file in os.listdir(f"{get_working_directory()}/analysis"):
        analysis_dir = f"{get_working_directory()}/analysis/{os.fsdecode(file)}"
        analyze_topology_file(analysis_dir, show_plots=show_plots)

def clean_key(key):
    if "__" in key:
        return key.split("__")[0]
    else:
        return key

def weighted(arr, weights):
    print(weights)
    total_weight = sum(weights)
    return [ a * w / total_weight for a, w in zip(arr, weights)]

def analyze_topology_file(analysis_dir, show_plots=True):
    topologies_filename = f"{analysis_dir}/topologies.txt"
    print(f"Processing {topologies_filename} ... ", flush=True)
    topologies, stats, runtimes, latencies = read_data(topologies_filename)
    # print(topologies)
    topo_throughputs = {}
    topo_latencies = {}
    topo_flow_size = {}
    for topo in topologies:
        topo_throughputs[clean_key(topo)] = []
        topo_latencies[clean_key(topo)] = []
        topo_flow_size[clean_key(topo)] = []
    for topo in topologies:
        fd = open(f"{get_working_directory()}/{topo}.pkl", "rb")
        network = pkl.load(fd)
        fd.close()
        fd = open(f"{analysis_dir}/{topo}_flowstats.txt", "w")
        server_total_throughput = {}
        server_latencies = {}
        #server_lengths = {}
        #server_flow_sizes = {}
        #server_runtimes = {}
        for node in network._node_map.values():
            if isinstance(node, Source):
                server_name = node.get_server_name()
                for flow in node._flows:
                    m_name = f"{topo}.{flow._src}.app[0]"
                    throughput_kb = flow._send_amount / runtimes[m_name] / 1000
                    fd.write(f"module={m_name} server={server_name} src={flow._src} dest={flow._dest} path_len={len(flow._path) - 3} throughput_kb={throughput_kb} latency_ms={latencies[m_name]} runtime={runtimes[m_name]} num_bytes={flow._send_amount}\n")  
                    topo_throughputs[clean_key(topo)].append(throughput_kb)
                    topo_latencies[clean_key(topo)].append(latencies[m_name])
                    topo_flow_size[clean_key(topo)].append(flow._send_amount)
                    if server_name in server_total_throughput.keys():
                        server_total_throughput[server_name] += throughput_kb
                        server_latencies[server_name].append(latencies[m_name])
                        #server_lengths[server_name].append(len(flow._path) - 3)
                        #server_flow_sizes[server_name].append(flow._send_amount)
                        #server_runtimes[server_name].append(runtimes[m_name])
                    else:
                        server_total_throughput[server_name] = throughput_kb
                        server_latencies[server_name] = [latencies[m_name]]
                        #server_lengths[server_name] = [len(flow._path) - 3]
                        #server_flow_sizes[server_name] = [flow._send_amount]
                        #server_runtimes[server_name] = [runtimes[m_name]]
        fd.close()
        
        for server_name, throughput_kb in server_total_throughput.items():
            if throughput_kb > LINK_RATE:  # Omnet++ seems to handle give too large of throughputs to small flows
                server_total_throughput[server_name] = LINK_RATE
        for key, value in stats.items():
            if key in topo:
                value['x'].extend(list(server_total_throughput.values()))
                value['y'].extend([np.mean(lats) for lats in server_latencies.values()])

    for topo in topo_throughputs.keys():
        if 'jitter' in topologies[0]:
            topo_flow_size[topo] = [ x + np.random.normal(0, 4000) for x in topo_flow_size[topo]]
        topo_throughputs[topo] = [ x / LINK_RATE for x in topo_throughputs[topo] ]
        topo_latencies[topo] = [ y / FATTREE_4_LATENCY for y in topo_latencies[topo] ]

    for topo in topo_throughputs.keys():  
        plt.scatter(topo_flow_size[topo], topo_latencies[topo], label=topo, s=10, alpha=0.5)
    plt.xlabel('Flow Size (B)')
    plt.ylabel('Normalized Latency (*)')
    plt.legend()
    plt.savefig(f"{analysis_dir}/latency_vs_size_plot.png")
    if show_plots:
        plt.show()
    plt.close()

    for topo in topo_throughputs.keys():  
        plt.scatter(topo_flow_size[topo], topo_throughputs[topo], label=topo, s=10, alpha=0.5)
    plt.xlabel('Flow Size (B)')
    plt.ylabel('Normalized Throughput (*)')
    plt.legend()
    plt.savefig(f"{analysis_dir}/throughput_vs_size_plot.png")
    if show_plots:
        plt.show()
    plt.close()

    analysis_str = ""
    for key, value in stats.items():
        # print(value['w'])
        xs = [ x / LINK_RATE for x in value['x']]
        ys = [ y / FATTREE_4_LATENCY for y in value['y']]
        prop_full_send = len([x for x in filter(lambda x: x == 1, xs)]) / len(xs)
        plt.scatter(xs, ys, label=clean_key(key), alpha=0.5, s=10)
        plt.errorbar(np.mean(xs), np.mean(ys), xerr=np.std(xs), yerr=np.std(ys), capsize=4)
        analysis_str += f"key={key} n={len(xs)} link_rate={LINK_RATE} fattree_latency={FATTREE_4_LATENCY} prop_full_send={prop_full_send}\n"
        analysis_str += f"Raw_X_Data: min={min(value['x'])} max={max(value['x'])} mean={np.mean(value['x'])} stdev={np.std(value['x'])}\n"
        analysis_str += f"Raw_Y_Data: min={min(value['y'])} max={max(value['y'])} mean={np.mean(value['y'])} stdev={np.std(value['y'])}\n"
        analysis_str += f"Normalized_X_Data: min={min(xs)} max={max(xs)} mean={np.mean(xs)} stdev={np.std(xs)}\n"
        analysis_str += f"Normalized_Y_Data: min={min(ys)} max={max(ys)} mean={np.mean(ys)} stdev={np.std(ys)}\n"
    
    analysis_file = open(f"{analysis_dir}/analysis.txt", "w")
    analysis_file.write(analysis_str)
    analysis_file.close()
    # print(analysis_str)

    plt.xlabel("Normalized Throughput (*)")
    plt.ylabel("Normalized Latency (*)")
    plt.legend()
    plt.savefig(f"{analysis_dir}/throughput_latency_plot.png")
    if show_plots:
        plt.show()


def get_cleaned_dfs(path):
    df = pd.read_csv(path)

    def timeavg_not_nan(row):
        if row['name'] == 'numActiveSessions:timeavg' and 'nan' not in str(row['value']):
            return True
        return False
    def vecvalue_not_nan(row):
        if row['name'] == 'endToEndDelay:vector' and 'nan' not in str(row['vecvalue']):
            return True
        return False
    
    df_times = df[df.apply(timeavg_not_nan, axis=1)]
    df_times.sort_values('module')
    df_delays = df[df.apply(vecvalue_not_nan, axis=1)]
    df_delays.sort_values('module')

    return df_times, df_delays

def read_data(topologies_filename):    
    # fd = open(f"{get_working_directory()}/topologies.txt", "r")
    fd = open(topologies_filename, "r")
    topologies = []
    stats = {}
    for line in fd.readlines():
        line = line.replace('\n', '')
        if "TRIAL" in line:
            continue
        line_data = {}
        for kv in line.split(" "):
            if "=" not in kv:
                if 'module' not in line_data:
                    line_data['module'] = kv
            else:
                key, value = kv.split("=")
                line_data[key] = value
        topologies.append(line_data['module'])
        stats[line_data['root']] = {
            'x': [],
            'y': []
        }
    fd.close()

    runtimes = {}
    latencies = {}

    for topo in topologies:
        df_times, df_delays = get_cleaned_dfs(f"{get_working_directory()}/results/{topo}.csv")

        for _, row in df_times.iterrows():
            runtimes[str(row['module'])] = SIMULATION_TIME * float(row['value'])

        for _, row in df_delays.iterrows():
            latencies[str(row['module'])] = np.mean([float(x) * 1000 for x in str(row['vecvalue']).split(" ")])
    
    return topologies, stats, runtimes, latencies

if __name__ == "__main__":
    main()