import bisect
import math
n = int(input())
infos = list(map(int, input().split()))


def solution():
    if infos[0] >= 0:
        return (infos[0], infos[1])
    if infos[-1] <= 0:
        return (infos[-2], infos[-1])
    partition = bisect.bisect_left(infos, 0)
    minimum = math.inf
    answer = None

    if partition+1 < n:
        temp = infos[partition]+infos[partition+1]
        if minimum > abs(temp):
            minimum = abs(temp)
            answer = (infos[partition], infos[partition+1])
    if partition-2 >= 0:
        temp = infos[partition-2]+infos[partition-1]
        if minimum > abs(temp):
            minimum = abs(temp)
            answer = (infos[partition-2], infos[partition-1])
    left = -1
    right = 0
    while left < partition:
        left += 1
        right = bisect.bisect_left(infos, -infos[left])
        if right != partition and (right-1) != left:
            temp = infos[left]+infos[right-1]
            if abs(minimum) > abs(temp):
                minimum = temp
                answer = (infos[left], infos[right-1])
        if right != n and right != left:
            temp = infos[left]+infos[right]
            if abs(minimum) > abs(temp):
                minimum = temp
                answer = (infos[left], infos[right])
    return answer


answer = solution()
print(' '.join(map(str, answer)))
