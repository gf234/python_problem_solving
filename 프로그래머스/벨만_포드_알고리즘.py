import sys
from collections import deque
import math

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((b, c))


def bellman_ford(start):
    dist = [math.inf for _ in range(N+1)]
    dist[start] = 0

    # n-1번 지나는 경로까지 계산하면 최단 경로를 얻을 수 있다.
    for _ in range(1, N):
        for here in range(1, N+1):
            for there, w in adj[here]:
                if adj[here] == math.inf:
                    continue
                if dist[there] > dist[here] + w:
                    dist[there] = dist[here] + w
    # 만약, 한번더 해서 바뀌면 음수 싸이클이 존재한다는 말이다.
    for here in range(1, N+1):
        for there, w in adj[here]:
            if adj[here] == math.inf:
                continue
            if dist[there] > dist[here] + w:
                print(-1)
                sys.exit()
    return dist


dist = bellman_ford(1)

for i in range(2, N+1):
    if dist[i] == math.inf:
        print(-1)
    else:
        print(dist[i])
