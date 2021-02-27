import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
indegrees = [0 for _ in range(n+1)]
for _ in range(m):
    cnt, *singers = map(int, input().split())
    for i in range(len(singers)):
        for j in range(i+1, len(singers)):
            adj[singers[i]].append(singers[j])
            indegrees[singers[j]] += 1

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

if len(answer) != n:
    print(0)
else:
    for x in answer:
        print(x)
