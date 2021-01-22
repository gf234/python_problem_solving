import sys
import heapq

while True:
    n, *h = map(int, input().split())

    if n == 0:
        break

    # 중간 막대를 포함한 넓이 중 가장 큰 값을 반환
    def calMaxArea(left, mid, right):
        i, j = mid, mid+1
        hh = min(h[mid], h[mid+1])
        maxArea = hh*2
        while i != left or j != right:
            if i == left:
                j += 1
                hh = min(hh, h[j])
            elif j == right:
                i -= 1
                hh = min(hh, h[i])
            else:
                if h[i-1] < h[j+1]:
                    j += 1
                    hh = min(hh, h[j])
                else:
                    i -= 1
                    hh = min(hh, h[i])
            maxArea = max(maxArea, hh*(j-i+1))
        return maxArea

    # 반씩 분할 하면서 값을 구한다.
    def maxArea(left, right):
        if left == right:
            return h[left]

        mid = left + (right-left)//2

        ret = max(maxArea(left, mid), maxArea(
            mid+1, right), calMaxArea(left, mid, right))

        return ret

    print(maxArea(0, n-1))
