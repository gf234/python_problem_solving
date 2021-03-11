import sys
import math
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m, fuel = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
x, y = map(int, input().split())
x -= 1
y -= 1
taxi = (x, y)


def findMinDist(start, destination):
    q = deque()
    q.append(start)
    dist = [[math.inf for _ in range(n)] for _ in range(n)]
    dist[start[0]][start[1]] = 0
    dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))
    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            nd = dist[x][y] + 1
            if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] != 1 and dist[nx][ny] > nd:
                if (nx, ny) == destination:
                    return nd
                dist[nx][ny] = nd
                q.append((nx, ny))
    return math.inf


destinations = dict()
distDestinations = dict()
for p in range(2, m+2):
    x, y, i, j = map(int, input().split())
    x -= 1
    y -= 1
    i -= 1
    j -= 1
    destinations[p] = (i, j)
    dist = findMinDist((x, y), (i, j))
    distDestinations[p] = dist
    mat[x][y] = p


def next():
    global taxi
    global fuel
    q = deque()
    q.append(taxi)
    dist = [[math.inf for _ in range(n)]for _ in range(n)]
    dist[taxi[0]][taxi[1]] = 0
    dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))
    customer = (math.inf, math.inf)
    minDist = math.inf
    while q:
        x, y = q.popleft()
        d = dist[x][y]

        if minDist < d:
            break

        if mat[x][y] != 0:
            minDist = d
            if customer[0] > x:
                customer = (x, y)
            elif customer[0] == x and customer[1] > y:
                customer = (x, y)
            continue

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            nd = dist[x][y] + 1
            if nd > fuel:
                break
            if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] != 1 and dist[nx][ny] > nd:
                dist[nx][ny] = nd
                q.append((nx, ny))
    if customer != (math.inf, math.inf):
        x, y = customer
        fuel -= minDist
        fuel -= distDestinations[mat[x][y]]
        if fuel >= 0:
            fuel += distDestinations[mat[x][y]]*2
            taxi = destinations[mat[x][y]]
            mat[x][y] = 0
            return True
        else:
            return False
    return False


for _ in range(m):
    if not next():
        print(-1)
        break
else:
    print(fuel)
