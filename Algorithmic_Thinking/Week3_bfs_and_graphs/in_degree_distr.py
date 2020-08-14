"""
Some basic graph stuff - including representation of directed grapgh as dictionary and computation og in_degreee
distrubtion.
"""
import math
import matplotlib.pyplot as plt

EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2:set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2:set([3]),3: set([0]), 4: set([1]), 5:set([2]), 6: set([]) }
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2:set([3,7]),3: set([7]),
           4: set([1]), 5:set([2]), 6: set([]), 7:set([3]), 8:set([1,2]), 9: set([0,4,5,6,7,3])}


def make_complete_graph(num_nodes):
    """
    Returns a directed graph with the desired number of nodes
    """
    graph = {}
    if num_nodes < 1:
        return graph
    for node in range(num_nodes):
        graph[node] = set()
        for other_node in range(num_nodes):
            if other_node != node:
                graph[node].add(other_node)
    return graph

#print make_complete_graph(10)


def compute_in_degrees(digraph):
    """
    Computes in-degress of directed graph.
    Return dictionary of the kind {node: indegree(node)}
    """
    in_degrees = {}

    for node in digraph.keys():
        in_degrees[node] = 0

    for head_set in digraph.values():
        for node in head_set:
            in_degrees[node] += 1
    return in_degrees

#print compute_in_degrees(EX_GRAPH2)


def in_degree_distribution(digraph):
    """ - Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the

     in-degrees of the graph. The function should return a dictionary whose keys correspond to in-degrees of nodes in
     the graph. The value associated with each particular in-degree is the number of nodes with that in-degree.
      In-degrees with no corresponding nodes in the graph are not included in the dictionary.
    print compute_in_degrees(EX_GRAPH1)
    """
    in_degrees = compute_in_degrees(digraph)
    distr = {}
    for in_degree in in_degrees.values():
        distr[in_degree] = distr.get(in_degree, 0) + 1
    print "computed unnormalied indegree distribution"
    return distr


def normalized_in_degree_distribution(digraph):
    """
    Takas a directed graph ans normalizes in_degree distribution.

    The degree distribution P(k) of a network is defined to be the fraction of nodes in the network with degree k.

    """
    in_degree_dist = in_degree_distribution(digraph)
    num_nodes = len(digraph)
    normalized_in_degree_dist = {}

    for key, val in in_degree_dist.items():
        normalized_in_degree_dist[key]= val/float(num_nodes)

    print "computed normalied indegree distribution"

    return normalized_in_degree_dist

def plot_dist(digraph, title, loglog = False):
    """
    Takes a directed graph and plots the points of the normalized in_degree_distribution
    """
    dist = normalized_in_degree_distribution(digraph)
    x_vals = []
    y_vals = []

    for key, value in dist.items():
        if key != 0:
            x_vals.append(key)
            y_vals.append(value)


    plt.plot(x_vals, y_vals, 'ro')

    if loglog:
        plt.xscale("log")
        plt.yscale("log")


    plt.xlabel('In-degrees')
    plt.ylabel('Frequency')

    plt.title("Normalized in_degree distribution of graph")

    plt.show()

#plot_dist(EX_GRAPH1, "no topic")
