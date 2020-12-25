# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A

    deq = deque(A)

    for _ in range(K):
        temp = deq.pop()
        deq.appendleft(temp)
    return list(deq)
