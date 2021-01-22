# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    zeroCount = 0
    answer = 0
    for x in A:
        if x == 0:
            zeroCount += 1
        else:
            answer += zeroCount
            if answer > 1000000000:
                return -1
    return answer
