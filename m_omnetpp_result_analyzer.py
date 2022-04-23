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

def main():
    show_plots = True
    if (len(sys.argv) > 2):
        print("Usage: main.py [omnet_working_dir]")
    if (len(sys.argv) >= 2):
        set_working_directory(sys.argv[1])    
    if (len(sys.argv) > 2):
        show_plots = False
    
    print(f"Working directory set to: \'{get_working_directory()}\'")
    analysis_dir = f"{get_working_directory()}/analysis"
    if not os.path.exists(analysis_dir):
        os.makedirs(analysis_dir)

    topologies, stats, runtimes, latencies = read_data()
    print(topologies)
    print(stats)
    for topo in topologies:
        fd = open(f"{get_working_directory()}/{topo}.pkl", "rb")
        network = pkl.load(fd)
        fd.close()
        fd = open(f"{get_working_directory()}/{topo}_flowstats.txt", "w")
        server_throughputs = {}
        server_latencies = {}
        server_lengths = {}
        server_flow_sizes = {}
        xs = []
        ys = []
        for node in network._node_map.values():
            if isinstance(node, Source):
                server_name = node.get_server_name()
                for flow in node._flows:
                    m_name = f"{topo}.{flow._src}.app[0]"
                    throughput_kb = flow._send_amount / runtimes[m_name] / 1000
                    fd.write(f"module={m_name} server={server_name} src={flow._src} dest={flow._dest} path_len={len(flow._path) - 3} throughput_kb={throughput_kb} latency_ms={latencies[m_name]} runtime={runtimes[m_name]} num_bytes={flow._send_amount}\n")  
                    xs.append(flow._send_amount)
                    ys.append(latencies[m_name])
                    if server_name in server_throughputs.keys():
                        server_throughputs[server_name] += throughput_kb
                        server_latencies[server_name].append(latencies[m_name])
                        server_lengths[server_name].append(len(flow._path) - 3)
                        server_flow_sizes[server_name].append(flow._send_amount)
                    else:
                        server_throughputs[server_name] = throughput_kb
                        server_latencies[server_name] = [latencies[m_name]]
                        server_lengths[server_name] = [len(flow._path) - 3]
                        server_flow_sizes[server_name] = [flow._send_amount]
        fd.close()
        plt.scatter(xs, ys, label=topo)
        for key, value in stats.items():
            if key in topo:
                print(key, topo)
                value['x'].extend(list(server_throughputs.values()))
                value['y'].extend([np.mean(lats) for lats in server_latencies.values()])

    plt.xlabel('flow size (B)')
    plt.ylabel('latency (ms)')
    plt.legend()
    plt.savefig(f"{analysis_dir}/size_latency_plot.png")
    if show_plots:
        plt.show()
    plt.close()

    analysis_str = ""
    for key, value in stats.items():
        plt.scatter(value['x'], value['y'], label=key)
        plt.errorbar(np.mean(value['x']), np.mean(value['y']), xerr=np.std(value['x']), yerr=np.std(value['y']), capsize=4, alpha=0.5)
        analysis_str += f"key={key}\n"
        analysis_str += f"X Data: n={len(value['x'])} min={min(value['x'])} max={max(value['x'])} mean={np.mean(value['x'])} stdev={np.std(value['x'])}\n"
        analysis_str+= f"Y Data: n={len(value['y'])} min={min(value['y'])} max={max(value['y'])} mean={np.mean(value['y'])} stdev={np.std(value['y'])}\n"
    
    analysis_file = open(f"{analysis_dir}/analysis.txt", "w")
    analysis_file.write(analysis_str)
    analysis_file.close()
    print(analysis_str)

    plt.xlabel("Throughput (kB/sec)")
    plt.ylabel("Latency (ms)")
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

def read_data():    
    fd = open(f"{get_working_directory()}/topologies.txt", "r")
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