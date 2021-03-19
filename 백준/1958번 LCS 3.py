import sys


def input(): return sys.stdin.readline().rstrip()


a = input()
b = input()
c = input()


def findlcs(a, b, c):
    cache = [[[0 for _ in range(len(c)+1)]
              for _ in range(len(b)+1)] for _ in range(len(a)+1)]

    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if a[i] == b[j] == c[k]:
                    cache[i+1][j+1][k+1] = cache[i][j][k] + 1
                else:
                    cache[i+1][j+1][k+1] = max(cache[i][j+1][k+1],
                                               cache[i+1][j][k+1], cache[i+1][j+1][k])
    return cache[-1][-1][-1]


print(findlcs(a, b, c))
