import math
from collections import defaultdict, deque
import sys

t = int(input())

for _ in range(t):
    l = int(sys.stdin.readline().rstrip())
    start = tuple(map(int, sys.stdin.readline().rstrip().split()))
    end = tuple(map(int, sys.stdin.readline().rstrip().split()))

    dxy = ((1, 2), (2, 1), (1, -2), (2, -1),
           (-1, 2), (-2, 1), (-1, -2), (-2, -1))

    q = deque()
    q.append(start)
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    while q:
        here = q.popleft()
        d = dist[here]

        if here == end:
            print(d)
            break

        for dir in range(8):
            there = (here[0]+dxy[dir][0], here[1]+dxy[dir][1])
            nd = d+1

            if 0 <= there[0] < l and 0 <= there[1] < l and dist[there] > nd:
                dist[there] = nd
                q.append(there)
