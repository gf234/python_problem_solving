def solution(n):
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = (cache[i-2] + cache[i-1]) % 1234567
    return cache[n]
    