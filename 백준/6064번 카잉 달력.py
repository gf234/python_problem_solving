import math

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    lcm = m*n//math.gcd(m, n)
    a, b = 1, 1
    answer = -1
    # a % m = x
    # a % n = y
    # a = m*? + x
    # a = n*? + y
    if m < n:
        m, n = n, m
        x, y = y, x
    if y == n:
        y = 0
    while True:
        if x <= lcm:
            if x % n == y:
                answer = x
                break
            x += m
        else:
            break

    print(answer)
