from collections import deque
import math
n, k = map(int, input().split())

MAX = 100000


def bfs(start, end):
    q = deque()
    q.append(start)

    dist = [math.inf for _ in range(MAX + 1)]
    dist[start] = 0

    while q:
        here = q.popleft()
        if here == end:
            return dist[here]
        ndist = dist[here] + 1

        there = here + 1
        if 0 <= there <= MAX:
            if dist[there] > ndist:
                dist[there] = ndist
                q.append(there)

        there = here - 1
        if 0 <= there <= MAX:
            if dist[there] > ndist:
                dist[there] = ndist
                q.append(there)

        there = here*2
        if 0 <= there <= MAX:
            if dist[there] > ndist:
                dist[there] = ndist
                q.append(there)


ans = bfs(n, k)

print(ans)
