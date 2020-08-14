import random
import in_degree_distr as idd
import matplotlib.pyplot as plt
def all_directed_pairs(num):
    """
    Returns a list of all directed pairs (i,j) of elements from {0, 1, ..., num-1}, where i != j.
    """
    answer = []
    for num1 in range(num):
        for num2 in range(num):
            if num1 != num2:
                answer.append((num1, num2))
    return answer

#print all_directed_pairs(2)

def make_ER_graph(num_nodes, prob):
    """
    Make a directed ER graph (represented as dictionary) with a certain number of nodes and a certain probability.
    """
    graph = {}

    for node in range(num_nodes):
        graph[node] = set()

    for pair in all_directed_pairs(num_nodes):
        if random.random() < prob:
            graph[pair[0]].add(pair[1])
    return graph



def plot_dist(digraph, n, p, normalized = False, loglog = False):
    """
    Takes a directed graph and plots the points of the normalized in_degree_distribution
    """
    if normalized:
        dist = idd.normalized_in_degree_distribution(digraph)
        title = "Normalized in-degree distribution of ER graph with n={} and p={}".format(n,p)
    else:
        dist = idd.in_degree_distribution(digraph)
        title = "Un-normalized in-degree distribution of ER graph with n={} and p={}".format(n,p)


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


    plt.title(title)

    plt.show()

#print make_ER_graph(10, 0.5)

##Plot log/log of normalized in-degree distribution
plot_dist(make_ER_graph(27700, 0.0005), 27700, 0.0005, True)
