import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m, t = map(int, input().split())
nums = [0]
for _ in range(n):
    row = deque(map(int, input().split()))
    nums.append(row)


def rotate(x, d, k):
    for i in range(x, n+1, x):
        for _ in range(k):
            if d == 0:
                temp = nums[i].pop()
                nums[i].appendleft(temp)
            else:
                temp = nums[i].popleft()
                nums[i].append(temp)


def remove():
    removePos = set()
    # 원판 내에서 인접하는 경우
    for i in range(1, n+1):
        for j in range(m-1):
            if nums[i][j] != 0 and nums[i][j] == nums[i][j-1]:
                removePos.add((i, j))
                removePos.add((i, j-1))
            if nums[i][j] != 0 and nums[i][j] == nums[i][j+1]:
                removePos.add((i, j))
                removePos.add((i, j+1))
        if nums[i][m-1] != 0 and nums[i][m-1] == nums[i][m-2]:
            removePos.add((i, m-1))
            removePos.add((i, m-2))
        if nums[i][m-1] != 0 and nums[i][m-1] == nums[i][0]:
            removePos.add((i, m-1))
            removePos.add((i, 0))
    # 다른 원판이 인접하는 경우
    for j in range(m):
        if n == 2:
            if nums[1][j] != 0 and nums[1][j] == nums[2][j]:
                removePos.add((1, j))
                removePos.add((2, j))
            continue

        for i in range(2, n):
            if nums[i][j] != 0 and nums[i][j] == nums[i-1][j]:
                removePos.add((i, j))
                removePos.add((i-1, j))
            if nums[i][j] != 0 and nums[i][j] == nums[i+1][j]:
                removePos.add((i, j))
                removePos.add((i+1, j))

    if removePos:
        for i, j in removePos:
            nums[i][j] = 0
    else:
        sum = 0
        cnt = 0
        changePos = []
        for i in range(1, n+1):
            for j in range(m):
                if nums[i][j] != 0:
                    cnt += 1
                    sum += nums[i][j]
                    changePos.append((i, j))
        if cnt:
            avg = sum / cnt
            for i, j in changePos:
                if nums[i][j] > avg:
                    nums[i][j] -= 1
                elif nums[i][j] < avg:
                    nums[i][j] += 1


for _ in range(t):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    remove()
answer = 0
for i in range(1, n+1):
    for j in range(m):
        answer += nums[i][j]
print(answer)
