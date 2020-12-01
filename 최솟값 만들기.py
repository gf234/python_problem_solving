def solution(A,B):
    n = len(A)
    sum = 0
    A.sort()
    B.sort()
    for i in range(n):
        sum += A[i] * B[n-1-i]
    return sum
