import math
import sys
from collections import defaultdict, deque
n, m = map(int, input().split())

adj = defaultdict(set)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].add(b)
    adj[b].add(a)


def bfs(start):
    q = deque()
    q.append(start)

    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    while q:
        here = q.popleft()

        for there in adj[here]:
            nDist = dist[here] + 1
            if dist[there] > nDist:
                dist[there] = nDist
                q.append(there)
    return sum(dist.values())


answer = -1
minVal = math.inf

for i in range(1, n+1):
    temp = bfs(i)
    if temp < minVal:
        minVal = temp
        answer = i
print(answer)
