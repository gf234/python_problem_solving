import sys
import heapq
import math

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    adj[u].append((v, w))

# 정점 번호 1 부터 시작


def bfs():
    q = []
    dist = [math.inf for _ in range(V+1)]
    dist[K] = 0
    heapq.heappush(q, (dist[K], K))

    while q:
        d, here = heapq.heappop(q)

        for there, w in adj[here]:
            ndist = d + w

            if dist[there] > ndist:
                dist[there] = ndist
                heapq.heappush(q, (dist[there], there))
    return dist


dist = bfs()

for i in range(1, V+1):
    if dist[i] == math.inf:
        print("INF")
    else:
        print(dist[i])
