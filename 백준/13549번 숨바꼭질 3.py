import math
import heapq

n, k = map(int, input().split())


def bfs():
    pq = []
    pq.append((0, n))
    dist = [math.inf for _ in range(100001)]
    dist[n] = 0

    while pq:
        hd, here = heapq.heappop(pq)

        there = here*2
        nd = hd
        if 0 <= there <= 100000 and dist[there] > nd:
            dist[there] = nd
            heapq.heappush(pq, (nd, there))

        there = here + 1
        nd = hd + 1
        if 0 <= there <= 100000 and dist[there] > nd:
            dist[there] = nd
            heapq.heappush(pq, (nd, there))

        there = here-1
        if 0 <= there <= 100000 and dist[there] > nd:
            dist[there] = nd
            heapq.heappush(pq, (nd, there))
    return dist


dist = bfs()
print(dist[k])
