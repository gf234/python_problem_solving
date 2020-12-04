def solution(n):
    DIV = 1234567

    cache = [0 for _ in range(n+2)]
    cache[1] = 1
    cache[2] = 2
    for i in range(3, n+1):
        cache[i] = (cache[i-1] + cache[i-2]) % DIV
    return cache[n]