import math
from itertools import combinations


def sum_subtree(num, node, childs):
    ret = num[node]

    for child in childs[node]:
        ret += sum_subtree(num, child, childs)
    return ret


def solution(k, num, links):
    n = len(num)

    exist_links = []
    for i, (left, right) in enumerate(links):
        if left != -1:
            exist_links.append((i, left))
        if right != -1:
            exist_links.append((i, right))

    num_exist_links = len(exist_links)
    answer = math.inf
    for temp_links in combinations(exist_links, num_exist_links-(k-1)):
        max_sum = 0

        parents = [-1 for _ in range(n)]
        childs = [[] for _ in range(n)]
        for parent, child in temp_links:
            parents[child] = parent
            childs[parent].append(child)

        for i in range(n):
            if parents[i] == -1:
                max_sum = max(max_sum, sum_subtree(num, i, childs))
        answer = min(answer, max_sum)
    return answer
