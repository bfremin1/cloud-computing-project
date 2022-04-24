import numpy as np
import matplotlib.pyplot as plt
import math

def plt_bisection_small():
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
    plt.savefig("graphs/bisection.png")
    plt.show()

def plt_bisection_repro():
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
    plt.savefig("graphs/bisection_repro.png")
    plt.show()

def main():
    plt_bisection_small()
    plt_bisection_repro()

if __name__ == "__main__":
    main()
