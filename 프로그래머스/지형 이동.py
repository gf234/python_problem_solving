from collections import defaultdict, deque
import heapq
import math


def solution(land, height):
    row = len(land)
    col = len(land[0])

    areaNums = [[-1 for _ in range(col)]for _ in range(row)]
    num = 0

    # 구역 나누기
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        areaNums[x][y] = num
        dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while q:
            hx, hy = q.popleft()
            h = land[hx][hy]

            for dx, dy in dxy:
                nx, ny = hx+dx, hy+dy
                if 0 <= nx < row and 0 <= ny < col:
                    if areaNums[nx][ny] == -1:
                        nh = land[nx][ny]
                        if abs(h-nh) <= height:
                            q.append((nx, ny))
                            areaNums[nx][ny] = num

    for i in range(row):
        for j in range(col):
            if areaNums[i][j] == -1:
                area = bfs(i, j)
                num += 1

    # 구역 사이의 비용 구하기
    costDict = defaultdict(lambda: math.inf)
    dxy = ((1, 0), (0, 1))
    for x in range(row):
        for y in range(col):
            aNum = areaNums[x][y]
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if 0 <= nx < row and 0 <= ny < col:
                    nNum = areaNums[nx][ny]
                    if aNum != nNum:
                        a, b = min(aNum, nNum), max(aNum, nNum)
                        costDict[(a, b)] = min(
                            costDict[(a, b)], abs(land[x][y] - land[nx][ny]))

    # 크루스칼 알고리즘으로 최소 스패닝 트리 찾기
    def find(parent, e):
        if parent[e] == e:
            return e
        parent[e] = find(parent, parent[e])
        return parent[e]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def kruskal(n, pq):
        parent = [i for i in range(n)]

        ret = 0

        while pq:
            cost, a, b = heapq.heappop(pq)

            if find(parent, a) != find(parent, b):
                union(parent, a, b)
                ret += cost
        return ret

    pq = []
    for key, val in costDict.items():
        a, b = key
        heapq.heappush(pq, (val, a, b))
    ans = kruskal(num, pq)
    return ans


land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1
print(solution(land, height))
