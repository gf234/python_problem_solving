import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
m = int(input())
mat = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if mat[i][k] == 1 and mat[k][j] == 1:
                mat[i][j] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if mat[i][j] == 0 and mat[j][i] == 0:
            cnt += 1
    print(cnt)
