import sys


def input(): return sys.stdin.readline().rstrip()


r, c, t = map(int, input().split())
mat = []
air = []
for i in range(r):
    row = list(map(int, input().split()))
    if row[0] == -1:
        air.append(i)
    mat.append(row)


def spread():
    temp = []
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    for i in range(r):
        for j in range(c):
            if mat[i][j] != -1 and mat[i][j] != 0:
                amount = mat[i][j] // 5
                sub = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and mat[x][y] != -1:
                        sub += amount
                        temp.append((x, y, amount))
                if sub != 0:
                    temp.append((i, j, -sub))
    while temp:
        i, j, x = temp.pop()
        mat[i][j] += x


def upClean():
    pos = [air[0], 1]
    temp = 0
    while pos[1] < c:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[1] += 1
    pos[0] -= 1
    pos[1] -= 1
    while pos[0] >= 0:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[0] -= 1
    pos[0] += 1
    pos[1] -= 1
    while pos[1] >= 0:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[1] -= 1
    pos[0] += 1
    pos[1] += 1
    while pos[0] < air[0]:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[0] += 1


def downClean():
    pos = [air[1], 1]
    temp = 0
    while pos[1] < c:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[1] += 1
    pos[0] += 1
    pos[1] -= 1
    while pos[0] < r:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[0] += 1
    pos[0] -= 1
    pos[1] -= 1
    while pos[1] >= 0:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[1] -= 1
    pos[0] -= 1
    pos[1] += 1
    while pos[0] > air[1]:
        i, j = pos
        mat[i][j], temp = temp, mat[i][j]
        pos[0] -= 1


for _ in range(t):
    spread()
    upClean()
    downClean()

answer = 0
for i in range(r):
    for j in range(c):
        if mat[i][j] != -1 and mat[i][j] != 0:
            answer += mat[i][j]
print(answer)
