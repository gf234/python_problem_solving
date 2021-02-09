import math
from collections import deque
import sys

n = int(input())

adj = [[] for _ in range(n)]
for _ in range(n):
    a, *infos = map(int, sys.stdin.readline().rstrip().split()[:-1])

    for i in range(0, len(infos), 2):
        b = infos[i]
        dist = infos[i+1]

        adj[a-1].append((b-1, dist))


def find_max_dist(start):
    q = deque()
    q.append(start)
    dist = [math.inf for _ in range(n)]
    dist[start] = 0
    ret_pos = -1
    ret_dist = -1
    while q:
        here = q.popleft()
        prev_dist = dist[here]

        for there, temp_dist in adj[here]:
            new_dist = prev_dist+temp_dist
            if dist[there] > new_dist:
                dist[there] = new_dist
                if ret_dist < new_dist:
                    ret_dist = new_dist
                    ret_pos = there
                q.append(there)
    return ret_pos, ret_dist


next_pos, _ = find_max_dist(0)
print(find_max_dist(next_pos)[1])
