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
    possibles = set()
    i = 0
    while True:
        temp = m*i + x
        if temp <= lcm:
            possibles.add(temp)
            i += 1
        else:
            break

    i = 0
    while True:
        temp = n*i + y
        if temp > lcm:
            break
        if temp in possibles:
            answer = temp
            break
        i += 1
    print(answer)
