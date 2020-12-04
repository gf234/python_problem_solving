from itertools import combinations
from collections import Counter


def solution(a):
    if len(a) < 2:
        return 0

    c = Counter(a)
    if len(c) < 2:
        return 0

    answer = 0

    for mcn, cnt in c.most_common():
        if answer >= cnt*2:
            break

        temp = 0
        i = 0
        while True:
            if i >= len(a)-1:
                break
            x, y = a[i], a[i+1]
            if (x != mcn and y == mcn) or (x == mcn and y != mcn):
                temp += 2
                i += 2
            else:
                i += 1
        answer = max(answer, temp)

    return answer


a = [4,0,0,2,1,1,1,1,1,1,0,3]
print(solution(a))
