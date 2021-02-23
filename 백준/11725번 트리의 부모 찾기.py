from collections import deque
import sys


def read(): return sys.stdin.readline().rstrip()


n = int(read())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, read().split())
    adj[a].append(b)
    adj[b].append(a)


def bfs():
    q = deque()
    q.append(1)
    visited = {1}

    parents = [1 for _ in range(n+1)]
    while q:
        here = q.popleft()

        for there in adj[here]:
            if there not in visited:
                visited.add(there)
                parents[there] = here
                q.append(there)
    return parents


parents = bfs()
for i in range(2, n+1):
    print(parents[i])
