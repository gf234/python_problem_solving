import sys
import heapq
import math

N, E = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())


def bfs(start):
    q = []
    dist = [math.inf for _ in range(N+1)]
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))

    while q:
        d, here = heapq.heappop(q)

        for there, w in adj[here]:
            ndist = d + w
            if dist[there] > ndist:
                dist[there] = ndist
                heapq.heappush(q, (dist[there], there))
    return dist


dist1 = bfs(1)
distV1 = bfs(v1)
distV2 = bfs(v2)

ans = math.inf
ans = min(dist1[v1]+distV1[v2]+distV2[N],
          dist1[v2] + distV2[v1]+distV1[N])

if ans == math.inf:
    print(-1)
else:
    print(ans)
