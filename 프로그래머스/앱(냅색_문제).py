import sys
import math
n, m = map(int, input().split())

using_bytes = [0]+list(map(int, sys.stdin.readline().rstrip().split()))
costs = [0]+list(map(int, sys.stdin.readline().rstrip().split()))

# dp[app][cost] : 최대 바이트
dp = [[0] * (sum(costs)+1) for _ in range(n+1)]

ans = math.inf

for i in range(n+1):
    for j in range(sum(costs)+1):
        if j >= costs[i]:
            dp[i][j] = max(dp[i-1][j-costs[i]]+using_bytes[i], dp[i-1][j])
            if dp[i][j] >= m:
                ans = min(ans, j)
        else:
            dp[i][j] = dp[i-1][j]

print(ans)
