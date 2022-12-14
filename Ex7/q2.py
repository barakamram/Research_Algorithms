
import matplotlib.pyplot as plt
import networkx as nx
import random as rd


# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques.html#networkx.algorithms.clique.find_cliques
def accurate(g):
    cliques = nx.find_cliques(g)
    max_clique = 0
    for clique in cliques:
        if max_clique < len(clique):
            max_clique = len(clique)
    return max_clique


# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.clique.max_clique.html#networkx.algorithms.approximation.clique.max_clique
def approximately(g):
    return len(nx.algorithms.approximation.clique.max_clique(g))


def draw(size, comp):
    plt.plot(size, comp)
    plt.ylabel('comp')
    plt.xlabel('size')
    plt.show()


def check_diff():
    size = []
    comp = []
    for n in range(10, 200):
        size.append(n)
        v = rd.randint(0, n)
        g = nx.fast_gnp_random_graph(n, v)
        comp.append(accurate(g)/approximately(g))
    draw(size, comp)


if __name__ == '__main__':
    check_diff()
