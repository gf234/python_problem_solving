import math
from collections import defaultdict, deque
t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    adj = [[] for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    s = int(input()) - 1

    def bfs(start):
        q = deque()
        q.append(start)
        dist = [math.inf for _ in range(n)]
        dist[start] = 0
        while q:
            here = q.popleft()
            d = dist[here]

            for there in adj[here]:
                if dist[there] > (d+6):
                    dist[there] = d+6
                    q.append(there)
        return dist

    dist = bfs(s)
    for i in range(n):
        if i == s:
            continue
        if dist[i] == math.inf:
            dist[i] = -1
        print(dist[i], end=' ')
    print()
