# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(X, Y, D):
    # write your code in Python 3.6
    # X + answer*D >= Y
    if X == Y:
        return 0
    else:
        return math.ceil((Y-X)/D)
