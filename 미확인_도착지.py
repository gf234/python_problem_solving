import sys
import heapq
import math

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        if a in (g, h) and b in (g, h):
            d = d*2 - 1
        else:
            d = d*2
        adj[a].append((b, d))
        adj[b].append((a, d))

    targets = []
    for _ in range(t):
        x = int(input())
        targets.append(x)

    def bfs(start):
        q = []
        dist = [math.inf for _ in range(n+1)]
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

    dist = bfs(s)

    ans = []

    for target in targets:
        if dist[target] != math.inf and dist[target] % 2 == 1:
            ans.append(target)

    ans.sort()


    for x in ans:
        print(x, end=" ")
    print()
