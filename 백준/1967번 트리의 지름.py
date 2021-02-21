import sys
from collections import deque
import math

n = int(input())

adj = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((b, w))
    adj[b].append((a, w))


def bfs(start):
    q = deque()
    q.append(start)

    dist = [math.inf for _ in range(n+1)]
    dist[start] = 0

    maxVal = 0
    maxNode = start
    while q:
        here = q.popleft()

        for there, d in adj[here]:
            nd = dist[here] + d
            if dist[there] > nd:
                dist[there] = nd
                q.append(there)
                if nd > maxVal:
                    maxVal = nd
                    maxNode = there
    return maxNode, maxVal

# 루트에서 가장 멀리있는 노드를 구하고 그 노드에서 가장 멀리있는 노드를 찾으면 트리의 지름이 된다.
temp, _ = bfs(1)
print(bfs(temp)[1])
