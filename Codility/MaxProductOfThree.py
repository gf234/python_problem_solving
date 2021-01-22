# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import bisect
import math


def solution(A):
    # write your code in Python 3.6
    A.sort()
    answer = -math.inf
    # 양수를 최대로 만들기
    # 다 양수
    if A[-1] > 0 and A[-2] > 0 and A[-3] > 0:
        answer = max(answer, A[-1]*A[-2]*A[-3])
    # 하나 양수 두개 음수
    if A[0] < 0 and A[1] < 0:
        answer = max(answer, A[0]*A[1]*A[-1])
    # 음수를 최소로 만들기
    if 0 in A:
        answer = max(answer, 0)
    else:
        i = bisect.bisect(A, 0)
        if i >= 3:
            answer = max(answer, A[i-1]*A[i-2]*A[i-3])
        elif i >= 1:
            answer = max(answer, A[i-1]*A[i]*A[i+1])
    return answer


while True:
    A = list(map(int, input().split()))
    print(solution(A))
