import sys
import math
import heapq

T = int(input())

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().rstrip().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().rstrip().split())
        adj[u].append((v, c, d))

    def dp():
        DP = [[math.inf]*(M+1) for _ in range(N+1)]
        DP[1][0] = 0
        for cost in range(M+1):
            for v in range(1, N+1):
                if DP[v][cost] == math.inf:
                    continue
                for there, c, d in adj[v]:
                    ndist = DP[v][cost] + d
                    ncost = c+cost
                    if ncost > M:
                        continue
                    if DP[there][ncost] > ndist:
                        DP[there][ncost] = ndist
        return DP

    DP = dp()

    ans = min(DP[N])

    if ans == math.inf:
        print("Poor KCM")
    else:
        print(ans)
