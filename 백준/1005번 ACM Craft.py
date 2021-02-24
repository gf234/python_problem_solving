import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    costs = [0] + list(map(int, input().split()))
    indegrees = [0 for _ in range(n+1)]
    adj = [[] for _ in range(n+1)]
    for i in range(k):
        a, b = map(int, input().split())
        indegrees[b] += 1
        adj[a].append(b)
    w = int(input())

    times = [0 for _ in range(n+1)]

    q = deque()
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
    print(times[w])
