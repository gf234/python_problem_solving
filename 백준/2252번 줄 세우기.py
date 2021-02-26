import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
adj = [[]for _ in range(n+1)]
indegrees = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegrees[b] += 1

q = deque()
for i in range(1, n+1):
    if indegrees[i] == 0:
        q.append(i)
answer = []
while q:
    here = q.popleft()
    answer.append(here)

    for there in adj[here]:
        indegrees[there] -= 1
        if indegrees[there] == 0:
            q.append(there)
print(' '.join(map(str, answer)))
