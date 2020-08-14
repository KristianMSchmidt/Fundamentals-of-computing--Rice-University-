"""
Programming exercises - to be used in applications.
KRMS 15/12/2017
"""

from collections import deque
import random

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the set consisting of all nodes that are visited
    by a breadth-first search that starts at start_node. (i.e. returns the connected component of the start node)

    Note that collections.deque module supports O(1) enqueue and dequeue operations, while pop(0) is O(n) in Python.
    Note: len() is = O(1) in Python (very fast)
    """

    queue = deque([start_node])
    visited = set([start_node])

    while len(queue) != 0:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.extend([neighbor])
    return visited


def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each set consists of all the nodes (and nothing else)
    in a connected component, and there is exactly one set in the list for each connected component in ugraph and nothing else.
    """
    remaining_nodes = set([node for node in ugraph.keys()])
    con_comps = []

    while len(remaining_nodes) != 0:
        node = random.sample(remaining_nodes, 1)[0]
        con_comp = bfs_visited(ugraph, node)
        con_comps.append(con_comp)
        remaining_nodes.difference_update(con_comp)
    return con_comps



#graph6 = {"a": set([7]), "b": set(["c"]), "c": set(["d","b"]), "d":set(["e", "c"]), "e":set(["d"]), 7: set(["a"]) }
#result = cc_visited(graph6)

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the largest connected
    component in ugraph.
    """
    max_size = 0
    for con_comp in cc_visited(ugraph):
        size = len(con_comp)
        if size > max_size:
            max_size = size
    return max_size

#print largest_cc_size(graph6)


def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph "ugraph", a list of nodes "attack_order" and iterates through the nodes in attack_order.
    For each node in the list, the function removes the given node and its edges from the graph and then computes the
    size of the largest connected component for the resulting graph. The function should return a list whose k+1th entry
    is the size of the largest connected component in the graph after the removal of the first k nodes in attack_order.
    The first entry (indexed by zero) is the size of the largest connected component in the original graph.

    The easiest method for implementing compute_resilience is to remove one node at a time and use largest_cc_size to
    compute the size of the largest connected component in the resulting graphs. This implementation has a running
    time of O(n(n+m)) where n is the number of nodes and m is the number of edges in the graph.
    """
    answer = []
    answer.append(largest_cc_size(ugraph))

    for attacked_node in attack_order:
        neighbors = ugraph[attacked_node]
        ugraph.pop(attacked_node)
        for neighbor in neighbors:
            ugraph[neighbor].remove(attacked_node)
        answer.append(largest_cc_size(ugraph))
    return answer

#print compute_resilience(graph6,["a","b", "c",7, "d","e"])
