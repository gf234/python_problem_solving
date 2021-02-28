import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n = int(input())
adj = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def find_parents():
    q = deque()
    q.append(1)
    levels = [-1 for _ in range(n+1)]
    levels[1] = 0
    parents = [-1 for _ in range(n+1)]
    while q:
        here = q.popleft()

        for there in adj[here]:
            level = levels[here] + 1
            if levels[there] == -1:
                q.append(there)
                levels[there] = level
                parents[there] = here
    return parents, levels


parents, levels = find_parents()


def find(a, b):
    if levels[a] < levels[b]:
        a, b = b, a
    while levels[a] != levels[b]:
        a = parents[a]

    if a == b:
        return a

    while True:
        a = parents[a]
        b = parents[b]
        if a == b:
            return a


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())

    answer = find(a, b)
    print(answer)
