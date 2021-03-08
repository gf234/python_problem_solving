import sys
import math
import heapq


def input(): return sys.stdin.readline().rstrip()


n, h, w = map(int, input().split())
mat = []
for _ in range(h):
    row = list(map(int, input().split()))
    mat.append(row)
risks = [0] + list(map(int, input().split()))
M = int(input())
units = [0]
unitMap = [[0 for _ in range(w)]for _ in range(h)]
for i in range(1, M+1):
    m, t, a, b = map(int, input().split())
    units.append((m, t, a, b))
    unitMap[a][b] = i
k = int(input())
commands = []
for _ in range(k):
    u, a, b = map(int, input().split())
    commands.append((u, a, b))


def battle(x, y, team):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and unitMap[nx][ny] != 0 and units[unitMap[nx][ny]][1] != team:
            return True
    return False


def bfs(u, a, b):
    move, team, c, d = units[u]
    q = []
    heapq.heappush(q, (0, c, d))
    dist = [[math.inf for _ in range(w)] for _ in range(h)]
    dist[c][d] = 0
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    while q:
        pd, x, y = heapq.heappop(q)
        if (x, y) != (c, d) and battle(x, y, team):
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and unitMap[nx][ny] == 0:
                nd = pd + risks[mat[nx][ny]]
                # 스테미너를 넘어서거나 이동할 수 없는 지역인 경우 넘어간다
                if nd > move or risks[mat[nx][ny]] == -1:
                    continue
                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))
                    # 목표 지점으로 갈 수 있는 경우 유닛을 이동시킨다.
                    if (nx, ny) == (a, b):
                        units[u] = (move, team, nx, ny)
                        unitMap[c][d] = 0
                        unitMap[nx][ny] = u
                        return


for u, a, b in commands:
    impossible = False
    if unitMap[a][b] != 0:
        impossible = True
    if risks[mat[a][b]] == -1:
        impossible = True
    if impossible:
        continue
    bfs(u, a, b)

for i in range(1, M+1):
    a, b = units[i][2], units[i][3]
    print(a, b)
