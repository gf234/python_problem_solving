import sys
import bisect


def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()
targets = list(map(int, input().split()))

parents = [i for i in range(m+1)]


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[x] = y


for target in targets:
    ind = bisect.bisect_right(cards, target)
    temp = find(ind)
    print(cards[temp])
    union(temp, temp+1)
