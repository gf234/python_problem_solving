# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binStr = bin(N)
    answer = 0
    cnt = 0

    for char in binStr[2:]:
        if char == '1':
            answer = max(answer, cnt)
            cnt = 0
        else:
            cnt += 1
    return answer
