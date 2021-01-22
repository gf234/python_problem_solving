import sys
import heapq

n = int(input())

left = []
right = []
mid = 0
for i in range(1, n+1):
    x = int(sys.stdin.readline().rstrip())

    # 처음 값을 중간으로 설정
    if i == 1:
        mid = x
    else:
        # mid를 기준으로 작은 값과 큰 값을 유지한다.
        if mid <= x:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)

        # 짝수
        if i % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
        # 홀수
        else:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)

    print(mid)
