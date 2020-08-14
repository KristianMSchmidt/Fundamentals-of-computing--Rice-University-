
"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane

KRMS. Last edited 20/12
"""

import math
import random
import alg_cluster as c
#from alg_cluster import Cluster

######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    answer = (float("inf"), -1, -1)

    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                answer = min(answer, pair_distance(cluster_list, idx1, idx2))
    return answer


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    length = len(cluster_list)

    if length <= 3:
        #print "cluster_list to slow", cluster_list
        answer = slow_closest_pair(cluster_list)
        #print "answer from slow", answer

    else:
        half_len = length/2

        left_half = cluster_list[:half_len]
        right_half = cluster_list[half_len:]
        #print "HER!!!!!!!!!!!!!!: ", right_half

        answer_left = fast_closest_pair(left_half)
        #print "answer_left", answer_left
        answer_right = fast_closest_pair(right_half)
        #print "answer_right", answer_right

        answer = min(answer_left, (answer_right[0], answer_right[1] + half_len, answer_right[2] + half_len))
        #print "min of right and left respec", answer
        #mid is approximate midpoint in horizontal direction
        mid = 0.5*(cluster_list[half_len - 1].horiz_center() + cluster_list[half_len].horiz_center())
        #print "mid", mid
        #print "half_width", answer[0]
        answer = min(answer, closest_pair_strip(cluster_list, mid, answer[0]))

    return answer

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    # """

    my_list = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width:
            #my_list.append((cluster_list[idx].vert_center(), idx))
            my_list.append(idx)
    my_list.sort(key = lambda idx: cluster_list[idx].vert_center())

    #print "my_list, indexes sorted after y coords", my_list
    answer = (float("inf"), -1, -1)

    num_clusters = len(my_list)

    for number1 in range(num_clusters - 1):
        for number2 in range(number1 + 1, min(number1 + 3, num_clusters - 1) + 1):
            #print number1, number2
            dist =  cluster_list[my_list[number1]].distance(cluster_list[my_list[number2]])
            #print "dist: ", dist
            #print ""
            answer = min(answer, (dist, min(my_list[number1], my_list[number2]), max(my_list[number1], my_list[number2])))
    return answer


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    #print ""
    #print "Computing hierarchical_clustering"
    #print ""
    current_length = len(cluster_list)

    while current_length > num_clusters:
    #    print "{} iterations left...".format(current_length - num_clusters)
        cluster_list.sort(key = lambda idx: idx.horiz_center())
        idx1, idx2 = fast_closest_pair(cluster_list)[1], fast_closest_pair(cluster_list)[2]
        cluster1 = cluster_list[idx1]
        cluster2 = cluster_list[idx2]
        cluster_list.remove(cluster2)
        cluster1.merge_clusters(cluster2)
        current_length -= 1
    return cluster_list

#
# def test():
#     """
#     simple tests on the way
#     """
#     cluster0 = c.Cluster(set(["Al"]), 1.1, 10,0,0)
#     cluster1 = c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
#     cluster2 = c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
#     cluster3 = c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)
#     cluster4 = c.Cluster(set(["NL"]), 5, 6,4,4)
#     cluster5 = c.Cluster(set(["NL"]), 5, 6.1, 100, 0.01)
#     cluster6 = c.Cluster(set(["hl"]), 6,13, 0,0)
#     cluster7 = c.Cluster(set(["hl"]), 6.5, 15, 0,0)
#     cluster8 = c.Cluster(set(["hl"]), 8, 13, 0,0)
#     print fast_closest_pair([cluster0, cluster1, cluster2,cluster3, cluster4, cluster5])
#     print len(hierarchical_clustering([cluster0, cluster1, cluster2,cluster3, cluster4, cluster5], 5))
# #test()


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters

    This function should compute an initial list of clusters (line 2 in the pseudo-code) with the property that each
    cluster consists of a single county chosen from the set of the num_cluster counties with the largest populations.

    As you implement KMeansClustering, here are a several items to keep in mind. In line 4, you should represent an
    empty cluster as a Cluster object whose set of counties is empty and whose total population is zero.
    The cluster centers my_f, computed by lines 2 and 8-9, should stay fixed as lines 5-7 are executed during one
    iteration of the outer loop. To avoid modifying these values during execution of lines 5-7, you should consider storing
    these cluster centers in a separate data structure. Line 7 should be implemented using the merge_clusters method
    from the Cluster class. merge_clusters will automatically update the cluster centers to their correct locations
    based on the relative populations of the merged clusters.
    """
    #print "Computing kmeans clustering of {} clusters. There are {} iterations, and the resulting number of clusters will be {}".format(len(cluster_list), num_iterations, num_clusters)

    copy = list(cluster_list)
    copy.sort(key = lambda idx: idx.total_population(), reverse = True)

    center_list = []
    for indx in range(num_clusters):
        high_pop_cluster = copy[indx]
        center_list.append((high_pop_cluster.horiz_center(), high_pop_cluster.vert_center()))

    for dummy1 in range(num_iterations):
    #    print "Computing iterations number", dummy1
        cluster_hub_list = []
        for dummy2 in range(num_clusters):
            cluster_hub_list.append(c.Cluster(set(), 0, 0, 0, 0))

        for idx in range(len(cluster_list)):
            cluster = cluster_list[idx]
            clusterx = cluster.horiz_center()
            clustery = cluster.vert_center()

            nearest_center_idx = None
            shortest_dist = float("inf")

            #find the center that is nearest to cluster
            for idx2 in range(len(center_list)):
                center = center_list[idx2]
                vert_dist = clusterx - center[0]
                horiz_dist = clustery - center[1]
                dist =  math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
                if dist < shortest_dist:
                    shortest_dist = dist
                    nearest_center_idx = idx2
            #print idx, nearest_center_idx
            #print cluster_hub_list[nearest_center_idx]
            #print cluster
            cluster_hub_list[nearest_center_idx].merge_clusters(cluster)

        for idx in range(num_clusters):
            new_center = (cluster_hub_list[idx].horiz_center(), cluster_hub_list[idx].vert_center())
            center_list[idx] = new_center

    return cluster_hub_list

# def test2():
#     """
#     Simple tests on the way
#     """
#     cluster0 = c.Cluster(set(["0"]), 0, 0, 10, 10)
#     cluster1 = c.Cluster(set(["1"]), 0, 2, 100, 10)
#     cluster2 = c.Cluster(set(["2"]), 10, 10, 10, 10)
#     cluster3 = c.Cluster(set(["3"]), 10, 8, 10, 10)
#     cluster4 = c.Cluster(set(["4"]), 0, 10, 10,10)
#     cluster5 = c.Cluster(set(["5"]), 5, 6, 20, 10)
#     #cluster6 = p.c.Cluster(set(["hl"]), 6,13, 0,0)
#     #cluster7 = p.c.Cluster(set(["hl"]), 6.5, 15, 0,0)
#     #cluster8 = p.c.Cluster(set(["hl"]), 8, 13, 0,0)
#     kmeans_clustering([cluster0, cluster1, cluster2, cluster3, cluster4, cluster5], 3, 3)
#
# #test2()

#print 0.2*10+0.2*10+0.2*8+0.4*
