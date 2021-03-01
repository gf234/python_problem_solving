import math
import sys

sys.setrecursionlimit(10**5)
d = int(input())

adj = [[] for _ in range(8)]
adj[0] = [1, 2]
adj[1] = [0, 2, 3]
adj[2] = [0, 1, 3, 4]
adj[3] = [1, 2, 4, 5]
adj[4] = [2, 3, 5, 6]
adj[5] = [3, 4, 7]
adj[6] = [4, 7]
adj[7] = [5, 6]
cache = [[-1 for _ in range(8)]for _ in range(100001)]


def dp(remain, pos):
    if cache[remain][pos] != -1:
        return cache[remain][pos]
    if remain == 0:
        if pos == 0:
            return 1
        else:
            return 0

    ret = 0
    for there in adj[pos]:
        ret = (ret + dp(remain-1, there)) % 1000000007
    cache[remain][pos] = ret
    return ret


answer = dp(d, 0)
print(answer)
