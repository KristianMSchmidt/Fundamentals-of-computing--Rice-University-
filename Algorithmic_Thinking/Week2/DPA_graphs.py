"""
Algorithm for building Random DPA graphs.
The final number of nodes, n=27770, should be equal to the total number of nodes in the physics theory paper.
The number of nodes in the initial complete graph, m, should be approx equal to the average out degree
in the physics citation graph (ie. m=13)

Implementation is a bit slow for lange numbers, but interely my own! See DPA provided for an easy trick to make algorithm faster
"""

import random
import numpy
import matplotlib.pyplot as plt
import in_degree_distr as idd


EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2:set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2:set([3]),3: set([0]), 4: set([1]), 5:set([2]), 6: set([]) }
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2:set([3,7]),3: set([7]),
           4: set([1]), 5:set([2]), 6: set([]), 7:set([3]), 8:set([1,2]), 9: set([0,4,5,6,7,3])}



def complete_graph(num_nodes):
    """
    Helper function
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


def compute_in_degs(digraph):
    """
    Computes in-degress of directed graph.
    Return dictionary of the kind {node: indegree(node)}
    """
    in_degs = {}

    for node in digraph.keys():
        in_degs[node] = 0

    for head_set in digraph.values():
        for node in head_set:
            in_degs[node] += 1

    return in_degs

#indegs = compute_in_degs(EX_GRAPH1)
#sum_indegs = sum(indegs.values())
#print sum_indegs

def DPA_graph(m, n):
    """
    Returns DPA graph with n nodes, build upon the initial complete graph with m nodes
    """
    current_graph = complete_graph(m)
    current_len_graph = m
    current_indegs = compute_in_degs(current_graph)
    current_sum_indegs = sum(current_indegs.values())

#    print "We start out with this complete graph of length {}:\n{}\n\n".format(current_len_graph,current_graph)

    for new_node in range(m, n):
        #print "current indgs", current_indegs
        #assert len(current_graph) == new_node, "laengde fejl"
#        print ""
        prob_list = [0]

        for indx in range(current_len_graph):
            prob_of_choosing_element = (current_indegs[indx] + 1)/float(current_sum_indegs + current_len_graph)
            prob_list.append(prob_list[indx] + prob_of_choosing_element)
#            print prob_list
        #print "prob_list for element nr {}: {}".format(new_node, prob_list)

        current_graph[new_node] = set()

        for indx in range(m):
            random_num = random.random()
            for indx2 in range(current_len_graph):
                if prob_list[indx2] <= random_num < prob_list[indx2 + 1]:
                    if indx2 not in current_graph[new_node]:
                        #print "new_node connecsts to {}".format(indx2)
                        current_graph[new_node].add(indx2)
                        current_indegs[indx2] += 1
                        current_sum_indegs += 1
                    #else:
                        #print "new node already connected to", indx2
                    #print "current_graph", current_graph
                    #print "current_indegs of:",indx2, current_indegs[indx2]

        current_indegs[new_node] = 0
        current_len_graph += 1

    return current_graph

#print DPA_graph(13,100)
print compute_in_degs(DPA_graph(13,200))


def plot_distr(digraph, m, n, normalized = True, loglog = True):
    """
    Takes a directed graph and plots the points of the normalized in_degree_distribution
    """
    if normalized:
        dist = idd.normalized_in_degree_distribution(digraph)
        title = "Normalized in-degree distribution of DPA graph with n={} and m={}".format(n,m)
    else:
        dist = idd.in_degree_distribution(digraph)
        title = "Un-normalized in-degree distribution of DPA graph with n={} and m={}".format(n,m)


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
        title += "\nlog/log-scale "

    plt.xlabel('In-degrees')
    plt.ylabel('Frequency')


    plt.title(title)

    plt.show()


##Plot log/log of normalized in-degree distribution
plot_distr(DPA_graph(2, 1347), 13, 27770, True, False)
