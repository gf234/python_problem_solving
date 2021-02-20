import math
import sys

t = int(input())
for _ in range(t):
    n, m, w = map(int, sys.stdin.readline().rstrip().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        adj[s].append((e, t))
        adj[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        adj[s].append((e, -t))

    def bellman_ford(start):
        dist = [math.inf for _ in range(n+1)]
        dist[start] = 0

        for _ in range(n-1):
            for here in range(1, n+1):
                for there, t in adj[here]:
                    if dist[there] > dist[here] + t:
                        visited.add(there)
                        dist[there] = dist[here] + t
        for here in range(1, n+1):
            for there, t in adj[here]:
                if dist[there] > dist[here] + t:
                    return True
        return False

    visited = set()
    for start in range(1, n+1):
        if start not in visited and bellman_ford(start):
            print('YES')
            break
    else:
        print('NO')
