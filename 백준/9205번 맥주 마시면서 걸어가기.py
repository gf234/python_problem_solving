from collections import deque
import sys

t = int(input())
for _ in range(t):
    # input
    n = int(sys.stdin.readline().rstrip())
    home = tuple(map(int, sys.stdin.readline().rstrip().split()))
    stores = []
    for _ in range(n):
        stores.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
    festival = tuple(map(int, sys.stdin.readline().rstrip().split()))
    infos = [home] + stores + [festival]

    def dist(a, b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

    # 행복하게 갈 수 있는 최대 거리 : 1000
    adj = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(i+1, n+2):
            if dist(infos[i], infos[j]) <= 1000:
                adj[i].append(j)
                adj[j].append(i)

    def bfs(start):
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        while q:
            here = q.popleft()

            for there in adj[here]:
                if there not in visited:
                    if there == n+1:
                        return "happy"
                    visited.add(there)
                    q.append(there)
        return "sad"

    print(bfs(0))
