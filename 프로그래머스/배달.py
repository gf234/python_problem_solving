import heapq
import math


def solution(N, road, K):
    adj = [list() for _ in range(N+1)]

    for a, b, c in road:
        adj[a].append((b, c))
        adj[b].append((a, c))

    q = []
    dist = [math.inf for _ in range(N+1)]
    dist[1] = 0
    heapq.heappush(q, (dist[1], 1))
    while q:
        hd, here = heapq.heappop(q)

        for there, d in adj[here]:
            nd = hd + d
            if dist[there] > nd:
                dist[there] = nd
                heapq.heappush(q, (nd, there))
    ans = 0
    for i in range(1, N+1):
        if dist[i] <= K:
            ans += 1
    return ans
