import sys

cache = dict()


def w(a, b, c):
    if (a, b, c) in cache:
        return cache[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b < c:
        ret = w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
        cache[(a, b, c)] = ret
        return ret
    ret = w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    cache[(a, b, c)] = ret
    return ret


while True:
    sinput = sys.stdin.readline()

    a, b, c = map(int, sinput.rstrip().split())

    if a == -1 and b == -1 and c == -1:
        break

    answer = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {answer}")
