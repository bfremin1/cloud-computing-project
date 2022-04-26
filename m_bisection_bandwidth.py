import sys, os
import numpy as np
import matplotlib.pyplot as plt
import math

STORAGE_DIR = "bisections/"

def plt_bisection_small():
    print("Generating plot for small k...")
    plt.gca().set_prop_cycle(None)
    for k in range(4, 10, 2):
        servers = []
        bandwidth = []
        n = 5 * (k ** 2) // 4
        for eta in np.arange(0.001, 1, 0.001):
            r = 4 / math.log2(((1 - eta) ** (1 - eta)) * ((1 + eta) ** (1 + eta)))
            if r > k:
                continue
            s = n * (k - r)
            b = (1 - eta) * r / (2 * (k - r))
            servers.append(s)
            bandwidth.append(b)
        plt.plot(servers, bandwidth, label = "Jellyfish: n = " + str(n) + ", k = " + str(k))
        plt.xlim([0, k ** 4 / 4 / 2])
        plt.ylim([0, 2])
    plt.gca().set_prop_cycle(None)
    for k in range(4, 10, 2):
        n = 5 * (k ** 2) // 4
        plt.plot([k ** 3 / 4], [1], marker='s', label = "FatTree: n = " + str(n) + ", k = " + str(k))
    plt.plot([0, k ** 4 / 4], [1, 1], alpha=0.4)
    plt.xlabel("Servers")
    plt.ylabel("Normalized Bisection Bandwidth")
    plt.legend()
    plt.savefig(STORAGE_DIR + "bisection_small.png")
    plt.show()
    plt.clf()

def plt_bisection_repro():
    print("Generating plot for large k (paper reproduction)...")
    plt.gca().set_prop_cycle(None)
    for k in [24, 32, 48]:
        servers = []
        bandwidth = []
        n = 5 * (k ** 2) // 4
        for eta in np.arange(0.001, 1, 0.001):
            r = 4 / math.log2(((1 - eta) ** (1 - eta)) * ((1 + eta) ** (1 + eta)))
            if r > k:
                continue
            s = n * (k - r)
            b = (1 - eta) * r / (2 * (k - r))
            servers.append(s)
            bandwidth.append(b)
        plt.plot(servers, bandwidth, label = "Jellyfish: n = " + str(n) + ", k = " + str(k))
        plt.xlim([0, 80000])
        plt.xticks(np.arange(0, 80001, 10000), np.arange(0, 81, 10))
        plt.ylim([0, 1.6])
    plt.gca().set_prop_cycle(None)
    for k in [24, 32, 48]:
        n = 5 * (k ** 2) // 4
        plt.plot([k ** 3 / 4], [1], marker='s', label = "FatTree: n = " + str(n) + ", k = " + str(k))
    plt.plot([0, k ** 4 / 4], [1, 1], alpha=0.4)
    plt.xlabel("Servers (Thousands)")
    plt.ylabel("Normalized Bisection Bandwidth")
    plt.legend()
    plt.savefig(STORAGE_DIR + "bisection_repro.png")
    plt.show()
    plt.clf()

def main():
    global STORAGE_DIR
    if len(sys.argv) > 1:
        STORAGE_DIR = sys.argv[1]
    if STORAGE_DIR[-1] != '/':
        STORAGE_DIR = STORAGE_DIR + '/'
    os.makedirs(STORAGE_DIR, exist_ok=True)
    plt_bisection_small()
    plt_bisection_repro()

if __name__ == "__main__":
    main()
