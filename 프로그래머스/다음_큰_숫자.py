def solution(n):
    c = bin(n).count('1')
    for m in range(n+1, 1000001):
        d = bin(m).count('1')
        if c == d:
            return m
