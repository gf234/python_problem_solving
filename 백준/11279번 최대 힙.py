import sys
import heapq

n = int(input())

hq = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(hq, -x)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
