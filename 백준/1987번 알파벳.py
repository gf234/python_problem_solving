import sys


def input(): return sys.stdin.readline().rstrip()


r, c = map(int, input().split())
mat = []
for _ in range(r):
    row = list(input())
    mat.append(row)


visited = [False for _ in range(26)]
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(x, y):
    ret = 1

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(mat[nx][ny])-ord('A')]:
            ind = ord(mat[nx][ny]) - ord('A')
            visited[ind] = True
            ret = max(ret, 1 + dfs(nx, ny))
            visited[ind] = False
    return ret


visited[ord(mat[0][0]) - ord('A')] = True
print(dfs(0, 0))
