# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(A):
    # write your code in Python 3.6
    n = len(A)

    sumA = [0 for _ in range(n)]
    sumA[0] = A[0]

    for i in range(1, n):
        sumA[i] = sumA[i-1] + A[i]

    answer = math.inf

    for p in range(1, n):
        answer = min(answer, abs(sumA[p-1]-(sumA[-1] - sumA[p-1])))

    return answer
