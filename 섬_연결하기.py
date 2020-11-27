import heapq


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


def solution(n, costs):
    if n == 1:
        return 0

    pq = []
    for a, b, c in costs:
        heapq.heappush(pq, (c, a, b))

    return kruskal(n, pq)
