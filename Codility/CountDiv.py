# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    # 제일 작은것 찾기
    minNum = -1
    if A % K == 0:
        minNum = A
    else:
        minNum = (A//K+1) * K

    return (B-minNum)//K + 1


A = 1
B = 2
K = 3
print(solution(A, B, K))
