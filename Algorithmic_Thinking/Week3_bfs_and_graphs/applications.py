"""
Code for Application portion of Module 2
Graph analysis, network resilience, running time analysis

Krisitian (and some provided code), 17/12/2017
Code is a bit messy
"""

# imports
import urllib2
import random
import time
import math
import in_degree_distr as idd
from project import compute_resilience
import matplotlib.pyplot as plt


############################################
# Provided code


#graph = {0:set([1,2,4,5]), 1:set([0,2]), 2:set([0,1,3]), 3:set([2]), 4:set([0]), 5:set([0])}

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        #bemark at "set" er afgoerende i nedenstaeende linje: Der skal laves en kopi, saa graphen ikke muteres
        new_graph[node] = set(graph[node])
    return new_graph

#print copy_graph(graph)

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)
    return order

#print targeted_order(graph)
#print graph

def fast_targeted_order(ugraph):
    """
    Does the same as the above, but faster
    """
    new_graph = copy_graph(ugraph)

    degree_sets = {}

    for possible_degree in range(len(new_graph)):
        degree_sets[possible_degree] = set()

    for node in new_graph:
        degree = len(new_graph[node])
        degree_sets[degree].add(node)

    answer = []

    for degree in range(len(new_graph) - 1, -1, -1):
        while len(degree_sets[degree]) > 0:
            important_node = random.sample(degree_sets[degree], 1)[0]
            degree_sets[degree].remove(important_node)

            for neighbor in new_graph[important_node]:
                neighbor_degree = len(new_graph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree - 1].add(neighbor)

            answer.append(important_node)
            delete_node(new_graph,important_node)

    return answer

#print fast_targeted_order(graph)
#print graph


##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#NETWORK = load_graph(NETWORK_URL)

## Number of edges in network:
def count_edges(ugraph):
    num_edges = 0
    for node in ugraph:
        #print node
        #print len(ugraph[node])
        num_edges += len(ugraph[node])
    return num_edges
#print "Number of edges in Network:", count_edges(NETWORK)
##6094

""""
Undirected ER-graphs
"""

def all_undirected_pairs(num):
    """
    Returns a list of all undirected pairs {i,j} of elements from {0, 1, ..., num-1}, where i != j.
    An undirected pair will (against convention) be presented as a tuple
    """
    answer = []
    for num1 in range(num):
        for num2 in range(num):
            if num2 > num1:
                answer.append((num1, num2))
    return answer

#print all_undirected_pairs(4)


def make_undirected_ER_graph(num_nodes, prob):
    """
    Make an undirected directed ER graph (represented as dictionary) with a certain number of nodes and a certain probability.
    """
    graph = {}

    for node in range(num_nodes):
        graph[node] = set()

    for pair in all_undirected_pairs(num_nodes):
        if random.random() < prob:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
    return graph

#print make_undirected_ER_graph(4, 0.5)



"""
Code to build an "Undirected DPA-graph", that is... an UPA-grapgh!"

"""



def complete_graph(num_nodes):
    """
    Helper function
    Returns a complete graph with the desired number of nodes
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
    Computes in-degress of graph.
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

def UPA_graph(m, n):
    """
    Returns UPA graph with n nodes, build upon the initial complete graph with m nodes
    Note that it is easier for new nodes to get further connections in a UPA than in DPA, since new nodes start out
    having non-zero indegree.

    Algorithm can be optimized for speed, see "DPA provided" for trick
    """
    assert m <= n, "m can't be bigger than n"
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

        current_indegs[new_node] = 0
        for indx in range(m):
            random_num = random.random()
            for indx2 in range(current_len_graph):
                if prob_list[indx2] <= random_num < prob_list[indx2 + 1]:
                    if indx2 not in current_graph[new_node]:
                        #print "new_node connecsts to {}".format(indx2)
                        current_graph[new_node].add(indx2)

                        #new_line
                        current_graph[indx2].add(new_node)

                        current_indegs[indx2] += 1

                        #new_line
                        current_indegs[new_node] += 1

                        current_sum_indegs += 2
                    #else:
                        #print "new node already connected to", indx2
                    #print "current_graph", current_graph
                    #print "current_indegs of:",indx2, current_indegs[indx2]

        current_len_graph += 1

    return current_graph

#print UPA_graph(4,6)
#print compute_in_degs(UPA_graph(4,10))




def plot_distr(digraph, m, n, normalized = True, loglog = True):
    """
    Takes a UPA graph with parameters n, m and plots the points of the normalized in_degree_distribution
    """
    if normalized:
        dist = idd.normalized_in_degree_distribution(digraph)
        title = "Normalized in-degree distribution of UPA graph with n={} and m={}".format(n,m)
    else:
        dist = idd.in_degree_distribution(digraph)
        title = "Un-normalized in-degree distribution of UPA graph with n={} and m={}".format(n,m)


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

#plot_distr(UPA_graph(2,1347), 4, 10, True, False)




"""
To begin, you should determine the probability p such that the ER graph computed using this edge probability has approximately
 the same number of edges as the computer network. (Your choice for p should be consistent with considering each edge
  in the undirected graph exactly once, not twice.)
"""
## Number of nodes and edges of the computer network
NUM_NODES_NETWORK = 1239
NUM_EDGES_NETWORK = 6094

## Maximal number of edges of undirected graph = n(n-1) = 6094
## Expected number of edges in undirected ER-graph(n,p) = n*(n-1)*p
## Calculate p such that number of edges of ER-graph apr. equal to 6094: p = 6094/(n(n-1)) = 6094/(1239*(1239-1))
#print (float(6094)/(1239*1238))

#print len(ER_GRAPH)
#print count_edges(ER_GRAPH)

"""
 Likewise, you should compute an integer m such that the number of edges in the UPA graph is close to the number of
 edges in the computer network. Remember that all three graphs being analyzed in this Application should have the same
 number of nodes and approximately the same number of edges.
"""
### I'll do this by trial and error.
def compute_average(m):
    summ = 0
    for dummy in range(50):
         summ += count_edges(UPA_graph(m,1239))
    return float(summ)/50

#print compute_average(2) #=4930,32
#print compute_average(3) #=7374
###I'll choose m = 2.


"""
Next, you should write a function random_order that takes a graph and returns a list of the nodes in the graph in some
 random order. Then, for each of the three graphs (computer network, ER, UPA), compute a random attack order using
 random_order and use this attack order in compute_resilience to compute the resilience of the graph.
"""

def random_order(graph):
    """
    Takes a graph and returns a list of the nodes in the graph in some
     random order.
    """
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes


"""
Once you have computed the resilience for all three graphs, plot the results as three curves combined in a single standard
plot (not log/log). Use a line plot for each curve. The horizontal axis for your single plot be the the number of nodes
removed (ranging from zero to the number of nodes in the graph) while the vertical axis should be the size of the largest
connect component in the graphs resulting from the node removal.
For this question (and others) involving multiple curves in a single plot, please include a legend in your plot that
distinguishes the three curves. The text labels in this legend should include the values for p and m that you used in
computing the ER and UPA graphs, respectively. Both matplotlib and simpleplot support these capabilities (matplotlib
 example and simpleplot example).
"""

def plot_resiliences():
    """
    Plots resiliences under random attack
    """

    #make graphs
    NETWORK = load_graph(NETWORK_URL)
    p = 0.0039729262
    ER_GRAPH = make_undirected_ER_graph(1239,p)
    UPA_GRAPH = UPA_graph(2, 1239)

    ##RESILIENCE OF ER_GRAPH
    RES_ER_GRAPH = compute_resilience(ER_GRAPH, random_order(ER_GRAPH))

    ##RESILIENCE OF UPA GRAPH
    RES_UPA_GRAPH = compute_resilience(UPA_GRAPH, random_order(UPA_GRAPH))

    ##RESILIENCE OF REAL NETWORK_GRAPH
    RES_NETWORK = compute_resilience(NETWORK, random_order(NETWORK))



    #ER_GRAPH
    x_vals = range(len(RES_ER_GRAPH))
    y_vals = RES_ER_GRAPH
    plt.plot(x_vals, y_vals, label = "ER-graph, p = 0.004)")

    #UPA_GRAPH
    x_vals = range(len(RES_UPA_GRAPH))
    y_vals = RES_UPA_GRAPH
    plt.plot(x_vals, y_vals, label = "UPA-graph, m = 2")

    #NETWORK
    x_vals = range(len(RES_NETWORK))
    y_vals = RES_NETWORK
    plt.plot(x_vals, y_vals, label = "Computer network")

    x_vals = range(1239+1)
    y_vals = [0.75 * (1239+1-number) for number in range(1239+1)]
    plt.plot(x_vals, y_vals, label = "Resilience limit")

    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of largest connected component')

    #tegner
    plt.legend()

    plt.title("Comparison of network resilience under random attack\n(Network size: 1239 nodes and 6094 edges)")

    #goer det hele synligt
    plt.show()

plot_resiliences()




##############################################################################
#Comparison of running time of targeted_order and fast_targeted_order

def plot_running_times():

    initial_num_nodes = 5
    x_vals = []
    y_1_vals = []
    y_2_vals = []

    for num_nodes in range(10, 1000, 10):
        graph = UPA_graph(initial_num_nodes, num_nodes)
        x_vals.append(num_nodes)

        # measure process time (= CPU time consumed) of "targeted_ord"
        t0 = time.clock()
        targeted_order(graph)
        y_1_vals.append(time.clock() - t0)

        # measure process time (= CPU time consumed) of "fast_targeted_order"
        t0 = time.clock()
        fast_targeted_order(graph)
        y_2_vals.append(time.clock() - t0)

    plt.plot(x_vals, y_1_vals, label = "Targeted_order")
    plt.plot(x_vals, y_2_vals, label = "Fast_targeted_order")

    plt.xlabel("Input size (number of nodes in UPA_graph)")
    plt.ylabel('CPU running time (sec.)')

    #tegner
    plt.legend()

    plt.title("Comparison of running times (desktop Python)")

    #goer det hele synligt
    plt.show()

#plot_running_times()




#####################################################
# Resilience under targeted attack

def plot_resiliences():
    """
    Plots resiliences under targeted attack
    """

    #Make graphs:
    p = 0.0039729262
    er_graph = make_undirected_ER_graph(1239, p)
    upa_graph = UPA_graph(2, 1239)
    network = load_graph(NETWORK_URL)

    #Compute resiliences under targeted_attack:
    res_ER_graph = compute_resilience(er_graph, fast_targeted_order(er_graph))
    res_UPA_graph = compute_resilience(upa_graph, fast_targeted_order(upa_graph))
    res_NETWORK = compute_resilience(network, fast_targeted_order(network))

    #plot data
    x_vals = range(1240)
    plt.plot(x_vals, res_ER_graph, label = "ER graph, p = 0.004")
    plt.plot(x_vals, res_UPA_graph, label = "UPA graph, m = 2")
    plt.plot(x_vals, res_NETWORK, label = "Real computer network")

    #plot resilience limit
    y_vals = [0.75 * (1239+1-number) for number in range(1239+1)]
    plt.plot(x_vals, y_vals, label = "Resilience limit")

    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of largest connected component')

    #tegner
    plt.legend()

    plt.title("Comparison of network resilience under targeted attack\n(Network size: 1239 nodes and 6094 edges)")

    #goer det hele synligt
    plt.show()

plot_resiliences()
