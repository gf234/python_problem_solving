# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    numSet = set()

    for num in A:
        if num in numSet:
            numSet.remove(num)
        else:
            numSet.add(num)

    return list(numSet)[0]
