# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(A):
    # write your code in Python 3.6
    # psums[i]: A[:i]까지의 합
    psums = [0]
    for i, num in enumerate(A):
        psums.append(psums[i]+num)

    minAvg = math.inf
    answer = -1
    for p in range(len(A)-1):
        q1 = p+2
        q2 = p+3

        avg1 = (psums[q1] - psums[p]) / (q1-p)
        if minAvg > avg1:
            minAvg = avg1
            answer = p
        if q2 <= len(A):
            avg2 = (psums[q2] - psums[p]) / (q2-p)
            if minAvg > avg2:
                minAvg = avg2
                answer = p
    return answer
