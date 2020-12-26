# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)+1
    nSum = (n*(n+1))//2
    return nSum - sum(A)
