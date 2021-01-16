import math
from collections import defaultdict, deque
import sys

t = int(input())

for _ in range(t):
    v, e = map(int, sys.stdin.readline().rstrip().split())

    adj = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    answer = "YES"

    color = dict()

    def bfs(start):
        q = deque()
        q.append(start)
        color[start] = True
        while q:
            here = q.popleft()
            c = color[here]

            for there in adj[here]:
                if there not in color:
                    color[there] = not c
                    q.append(there)
                elif color[there] == c:
                    return False
        return True

    for i in range(v):
        if i not in color:
            if not bfs(i):
                answer = "NO"
                break

    print(answer)
