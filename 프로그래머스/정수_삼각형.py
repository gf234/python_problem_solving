cache = [[-1 for _ in range(10000)]for _ in range(501)]
maxH = -1


def recur(triangle, h, n):
    global cache

    if h+1 == maxH:
        return triangle[h][n]

    if cache[h][n] != -1:
        return cache[h][n]

    cache[h][n] = triangle[h][n] + max(recur(triangle, h+1, n), recur(triangle, h+1, n+1))
    return cache[h][n]


def solution(triangle):
    answer = 0

    global maxH
    maxH = len(triangle)

    answer = recur(triangle, 0, 0)

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))
