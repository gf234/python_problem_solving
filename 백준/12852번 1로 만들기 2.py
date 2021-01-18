import math
from collections import defaultdict, deque

x = int(input())


def bfs(start):
    q = deque()
    q.append(start)
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    parent = dict()
    parent[start] = -1
    while q:
        here = q.popleft()
        d = dist[here]

        if here == 1:
            break

        if here % 3 == 0:
            there = here//3
            if dist[there] > (d+1):
                dist[there] = d+1
                parent[there] = here
                q.append(there)

        if here % 2 == 0:
            there = here//2
            if dist[there] > (d+1):
                dist[there] = d+1
                parent[there] = here
                q.append(there)

        there = here-1
        if dist[there] > (d+1):
            dist[there] = d+1
            parent[there] = here
            q.append(there)

    answer = []
    num = 1
    while num != -1:
        answer.append(num)
        num = parent[num]
    answer.reverse()
    print(dist[1])
    print(" ".join(map(str, answer)))


bfs(x)
