import sys


N, M, K = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    A.append(row)
max_age = 0
trees = [[[5 if i == 0 else 0 for i in range(
    200)] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    max_age = max(max_age, z)
    trees[x-1][y-1][z] += 1


ans = M

dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for _ in range(K):
    if ans == 0:
        break

    def spring():
        global max_age
        deadTree = []
        for i in range(N):
            for j in range(N):
                aging = []
                for k in range(1, max_age+1):
                    treeCnt = trees[i][j][k]
                    if treeCnt == 0:
                        continue
                    if trees[i][j][0] >= treeCnt*k:
                        trees[i][j][0] -= treeCnt*k
                        trees[i][j][k] -= treeCnt
                        aging.append((k+1, treeCnt))
                    else:
                        live = 0
                        sum = k
                        while trees[i][j][0] >= sum:
                            live += 1
                            sum += k
                        trees[i][j][0] -= live*k
                        trees[i][j][k] -= treeCnt
                        aging.append((k+1, live))
                        deadTree.append((i, j, k//2, treeCnt-live))
                for age, cnt in aging:
                    if age > max_age:
                        max_age = age
                    trees[i][j][age] += cnt
        return deadTree

    deadTree = spring()

    def summer(deadTree):
        global ans
        for i, j, k, cnt in deadTree:
            ans -= cnt
            trees[i][j][0] += k*cnt

    summer(deadTree)

    def fall():
        global ans
        for i in range(N):
            for j in range(N):
                for k in range(5, max_age+1, 5):
                    cnt = trees[i][j][k]
                    for di, dj in dir:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            ans += cnt
                            trees[ni][nj][1] += cnt

    fall()

    def winter():
        for i in range(N):
            for j in range(N):
                trees[i][j][0] += A[i][j]

    winter()


print(ans)
