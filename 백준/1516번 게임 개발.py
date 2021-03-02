import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n = int(input())
indegrees = [0 for _ in range(n+1)]
costs = [0 for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    cost, *requires = map(int, input().split())
    costs[i] = cost
    for j in requires:
        if j == -1:
            break
        adj[j].append(i)
        indegrees[i] += 1

q = deque()
times = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if indegrees[i] == 0:
        q.append(i)
        times[i] = costs[i]

while q:
    here = q.popleft()

    for there in adj[here]:
        times[there] = max(times[there], times[here] + costs[there])
        indegrees[there] -= 1
        if indegrees[there] == 0:
            q.append(there)

for i in range(1, n+1):
    print(times[i])
