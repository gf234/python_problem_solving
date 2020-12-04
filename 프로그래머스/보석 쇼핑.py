from collections import defaultdict
import heapq


def solution(gems):
    gl = len(gems)
    gcnt = len(set(gems))

    start = 0
    end = 0

    tempSet = defaultdict(lambda: 0)
    possible = []
    while True:
        if start > end:
            break
        if len(tempSet) == gcnt:
            heapq.heappush(possible, (end-start, [start+1, end]))
            tempSet[gems[start]] -= 1
            if tempSet[gems[start]] == 0:
                tempSet.pop(gems[start])
            start += 1
        elif end == gl:
            break
        else:
            tempSet[gems[end]] += 1
            end += 1
    return possible[0][1]


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
