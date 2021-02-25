from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
indegrees = [0]
costs = [0]
adj = [[]for _ in range(n+1)]
for b in range(1, n+1):
    cost, indegree, *precedents = map(int, input().split())
    for a in precedents:
        adj[a].append(b)

    costs.append(cost)
    indegrees.append(indegree)

q = deque()
times = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if indegrees[i] == 0:
        times[i] = costs[i]
        q.append(i)

while q:
    here = q.popleft()

    for there in adj[here]:
        times[there] = max(times[there], times[here] + costs[there])
        indegrees[there] -= 1
        if indegrees[there] == 0:
            q.append(there)

print(max(times))
