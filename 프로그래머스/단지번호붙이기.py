n = int(input())

mat = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(i, j, mat):
    ret = 1
    mat[i][j] = 0

    for x, y in dir:
        ni = x+i
        nj = y+j

        if 0 <= ni < n and 0 <= nj < n:
            if mat[ni][nj] == 1:
                ret += dfs(ni, nj, mat)

    return ret


ans = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            ans.append(dfs(i, j, mat))

ans.sort()
print(len(ans))

for x in ans:
    print(x)
