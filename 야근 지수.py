import heapq


def solution(n, works):
    answer = 0

    works = [-i for i in works]
    heapq.heapify(works)

    for _ in range(n):
        m = heapq.heappop(works)
        m += 1
        heapq.heappush(works, m)

    for w in works:
        if w < 0:
            answer += w**2

    return answer
