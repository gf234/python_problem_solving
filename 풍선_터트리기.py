import heapq


def solution(a):
    baloons = [(b, i) for i, b in enumerate(a)]
    cnt = len(a)
    left = baloons[:1]
    right = baloons[1:]
    heapq.heapify(left)
    heapq.heapify(right)

    for i, b in enumerate(a[1:-1], 1):
        lmin, li = left[0]
        rmin, ri = right[0]
        while ri <= i:
            heapq.heappop(right)
            rmin, ri = right[0]

        if lmin < b and rmin < b:
            cnt -= 1

        heapq.heappush(left, (b, i))
    return cnt


a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(a))
