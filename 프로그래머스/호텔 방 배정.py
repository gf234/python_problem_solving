import sys

sys.setrecursionlimit(200000)


def solution(k, room_number):
    parent = dict()

    def find(x):
        if x not in parent:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    answer = []

    for x in room_number:
        if x not in parent:
            answer.append(x)
            parent[x] = x+1
        else:
            p = find(x)
            answer.append(p)
            parent[p] = p+1
    return answer
