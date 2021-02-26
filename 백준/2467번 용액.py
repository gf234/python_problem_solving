import bisect
import math
n = int(input())
infos = list(map(int, input().split()))


def solution():
    # 모두 양수인 경우
    if infos[0] >= 0:
        return (infos[0], infos[1])
    # 모두 음수인 경우
    if infos[-1] <= 0:
        return (infos[-2], infos[-1])
    # 양수와 음수를 나누는 지점을 구한다.
    partition = bisect.bisect_left(infos, 0)
    minimum = math.inf
    answer = None
    # 모두 양수가 답인 경우
    if partition+1 < n:
        temp = infos[partition]+infos[partition+1]
        if minimum > abs(temp):
            minimum = abs(temp)
            answer = (infos[partition], infos[partition+1])
    # 모두 음수가 답인 경우
    if partition-2 >= 0:
        temp = infos[partition-2]+infos[partition-1]
        if minimum > abs(temp):
            minimum = abs(temp)
            answer = (infos[partition-2], infos[partition-1])
    # 음수와 양수로 이루어진 값이 답인경우
    left = 0
    right = 0
    while left < partition:
        # 이분탐색으로 음수 값을 양수로 바꾼 값보다 크거나 같은 가장 가까운 점을 찾는다.
        right = bisect.bisect_left(infos, -infos[left])
        # 이분탐색으로 찾은 값과 그 이전값이 답의 후보가 된다.
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
        left += 1
    return answer


answer = solution()
print(' '.join(map(str, answer)))
