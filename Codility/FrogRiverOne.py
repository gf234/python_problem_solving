# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    numSet = set()

    for i, num in enumerate(A):
        numSet.add(num)
        if len(numSet) == X:
            return i
    return -1
