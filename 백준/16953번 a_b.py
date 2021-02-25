from collections import defaultdict, deque
import math

a, b = map(int, input().split())


def solve(a, b):
    q = deque()
    q.append(a)
    dist = defaultdict(lambda: math.inf)
    dist[a] = 1
    while q:
        here = q.popleft()
        if here == b:
            break

        there = here*2
        if there <= 1000000000 and there not in dist:
            dist[there] = dist[here] + 1
            q.append(there)

        there = here*10 + 1
        if there <= 1000000000 and there not in dist:
            dist[there] = dist[here] + 1
            q.append(there)

    if b not in dist:
        return -1
    return dist[b]


print(solve(a, b))
