import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n = int(input())
adj = [[] for _ in range(n+1)]
degrees = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b, dist = map(int, input().split())
    adj[a].append((b, dist))
    adj[b].append((a, dist))
    degrees[a] += 1
    degrees[b] += 1
# 연결된 개수가 3개 미만이면 루트가 될 수 있다.
root = -1
for i in range(1, n+1):
    if degrees[i] < 3:
        root = i
        break


def findLevelsAndParents():
    levels = [0 for _ in range(n+1)]
    parents = [(i, 0) for i in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[root] = True
    q = deque()
    q.append(root)
    while q:
        here = q.popleft()

        for there, dist in adj[here]:
            if not visited[there]:
                levels[there] = levels[here] + 1
                parents[there] = (here, dist)
                visited[there] = True
                q.append(there)
    return levels, parents


levels, parents = findLevelsAndParents()


def solve(a, b):
    dist = 0
    if levels[a] < levels[b]:
        a, b = b, a

    while levels[a] != levels[b]:
        dist += parents[a][1]
        a = parents[a][0]

    while True:
        if a == b:
            return dist

        dist += parents[a][1]
        a = parents[a][0]

        dist += parents[b][1]
        b = parents[b][0]


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(solve(a, b))
