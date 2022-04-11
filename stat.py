import sys
import numpy as np
import pandas as pd

if len(sys.argv) != 4:
    print("usage: python stat.py <omnet.ini> <results.sca> <results.vec>\n")
    exit()

with open(sys.argv[1], 'r') as ini:
    for line in ini:
        entry = line.split()
        if len(entry) != 0 and entry[0] == "sim-time-limit":
            sim_time = int(''.join(c for c in entry[2] if c.isdigit()))
            break
with open(sys.argv[2], 'r') as scalars:
    for line in scalars:
        entry = line.split()
        if len(entry) != 0 and entry[0] == "scalar" and entry[2] == "numActiveSessions:timeavg":
            print("host", entry[1], "session_time", float(entry[3]) * sim_time, "s")
with open(sys.argv[3], 'r') as vectors:
    flows = []
    vecs = []
    for line in vectors:
        entry = line.split()
        if len(entry) != 0 and entry[0] == "vector" and entry[3] == "endToEndDelay:vector":
            flows.append([entry[2], entry[3], entry[1], []])
            vecs.append(entry[1])
        elif len(entry) != 0 and entry[0] in vecs:
            flows[vecs.index(entry[0])][3].append(float(entry[3]))
    for flow in flows:        
        print("host", flow[0], "mean_latency", np.mean(flow[3]), "s")

