def solution(n):
    ans = 0

    while n:
        if n % 2 != 0:
            ans += 1
        n //= 2
    return ans


while True:
    n = int(input())
    if n == -1:
        break
    print(solution(n))
