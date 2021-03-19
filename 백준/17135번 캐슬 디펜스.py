import sys
import math
import copy
from itertools import combinations
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m, d = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
archers = []


def find(pos, mat):
    q = deque()
    q.append((n-1, pos))
    dist = [[math.inf for _ in range(m)] for _ in range(n)]
    dist[n-1][pos] = 1
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    mindist = math.inf
    temp = []
    if mat[n-1][pos] == 1:
        temp.append((n-1, pos))
        mindist = 1
    while q:
        x, y = q.popleft()

        if dist[x][y] == mindist:
            continue

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            nd = dist[x][y] + 1
            if nd > d:
                break
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] > nd:
                dist[nx][ny] = nd
                q.append((nx, ny))
                if mat[nx][ny] == 1:
                    temp.append((nx, ny))
                    mindist = nd
    if mindist == math.inf:
        return None
    temp.sort(key=lambda x: x[1])
    return temp[0]


def shoot(archers, mat):
    cnt = 0
    attack = set()
    for pos in archers:
        enemy = find(pos, mat)
        if enemy == None:
            continue
        attack.add(enemy)
    for x, y in attack:
        mat[x][y] = 0
        cnt += 1
    return cnt


def move(mat):
    ret = False
    for j in range(m):
        temp = 0
        for i in range(n):
            temp, mat[i][j] = mat[i][j], temp
            if mat[i][j] == 1:
                ret = True
    return ret


def solve(mat):
    temp = [i for i in range(m)]
    combs = combinations(temp, 3)
    answer = 0
    original = copy.deepcopy(mat)
    for archers in combs:
        cnt = 0
        while True:
            cnt += shoot(archers, mat)
            if not move(mat):
                break
        if answer < cnt:
            answer = cnt
        mat = copy.deepcopy(original)
    return answer


print(solve(mat))
