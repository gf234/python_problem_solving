import sys

sys.setrecursionlimit(100001)
nums = list(map(int, input().split()))


dp = [[[-1 for _ in range(100001)]for _ in range(5)]for _ in range(5)]


def cost(x, pos):
    if pos == 0:
        return 2

    diff = abs(pos-x)
    if diff == 0:
        return 1
    if diff == 2:
        return 4
    return 3


def recur(left, right, i):
    x = nums[i]
    if x == 0:
        return 0
    if dp[left][right][i] != -1:
        return dp[left][right][i]
    # 왼쪽을 움직이는 경우
    ltemp = recur(x, right, i+1) + cost(x, left)
    # 오른쪽을 움직이는 경우
    rtemp = recur(left, x, i+1) + cost(x, right)
    dp[left][right][i] = min(ltemp, rtemp)
    return dp[left][right][i]


print(recur(0, 0, 0))
