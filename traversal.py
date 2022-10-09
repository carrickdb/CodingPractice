#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'distinctTraversal' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
import heapq


def distinctTraversal(g_nodes, g_from, g_to):
    nodes = set(g_from)
    nodes = list(nodes.union(set(g_to)))
    edges = {}
    for i in range(len(g_from)):
        node = g_from[i]
        if node not in edges:
            edges[node] = []
        otherNode = g_to[i]
        edges[node].append(otherNode)
        if otherNode not in edges:
            edges[otherNode] = []
        edges[otherNode].append(node)
    visited = set()
    path = []
    curr = max(nodes)
    h = [-1*curr]
    heapq.heapify(h)
    while len(visited) < g_nodes:
        print(h)
        curr = heapq.heappop(h)*-1
        visited.add(curr)
        path.append(curr)
        for child in edges[curr]:
            if child not in visited:
                heapq.heappush(h, -1*child)
    return path

fromNodes = [2,4,6,7,1]
toNodes =   [4,6,1,4,7]
print(distinctTraversal(5, fromNodes, toNodes))
