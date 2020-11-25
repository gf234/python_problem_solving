import sys
import math

N = int(input())

mat = []
for _ in range(N):
    nums = list(map(int, input().split()))
    mat.append(nums)

ans = math.inf

dp = [[math.inf for _ in range((1 << N))] for _ in range(N)]


def recur(here, bit):
    if bit == ((1 << N)-1):
        if mat[here][0] != 0:
            return mat[here][0]
        else:
            return math.inf

    if dp[here][bit] != math.inf:
        return dp[here][bit]

    for there, cost in enumerate(mat[here]):
        if cost != 0:
            if bit & (1 << there) == 0:
                dp[here][bit] = min(dp[here][bit], cost +
                                    recur(there, bit | (1 << there)))
    return dp[here][bit]


ans = recur(0, 1)

print(ans)
