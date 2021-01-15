import sys
import heapq

n = int(input())

left = []
right = []
mid = 0
for i in range(1, n+1):
    x = int(sys.stdin.readline().rstrip())

    if i == 1:
        mid = x
    else:
        if mid <= x:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)

        # 짝수
        if i % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
        else:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)

    print(mid)
