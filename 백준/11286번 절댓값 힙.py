import sys
import heapq

n = int(input())

hq = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            _, o = heapq.heappop(hq)
            print(o)
        else:
            print(0)
