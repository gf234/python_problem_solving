#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    adj = [[] for _ in range(graph_nodes)]
    for i in range(len(graph_from)):
        adj[graph_from[i]-1].append(graph_to[i]-1)
        adj[graph_to[i]-1].append(graph_from[i]-1)

    def bfs(start, ids, val):
        q = deque()
        q.append(start)
        dist = defaultdict(lambda: math.inf)
        dist[start] = 0
        while q:
            here = q.popleft()
            d = dist[here]

            for there in adj[here]:
                if dist[there] > (d+1):
                    if ids[there] == val:
                        return d+1
                    dist[there] = d+1
                    q.append(there)
        return math.inf

    answer = math.inf
    for i in range(graph_nodes):
        if ids[i] == val:
            answer = min(answer, bfs(i, ids, val))

    if answer == math.inf:
        answer = -1
    return answer


if __name__ == '__main__':
    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(ans)
