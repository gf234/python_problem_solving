import sys
import math

V, E = map(int, input().split())

adj = [[math.inf for j in range(V+1)] for i in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c


def all_path():
    for v in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if i == v or j == v:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][v] + adj[v][j])


all_path()

ans = math.inf
for i in range(1, V+1):
    ans = min(ans, adj[i][i])

if ans == math.inf:
    print(-1)
else:
    print(ans)
