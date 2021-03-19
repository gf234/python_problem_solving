import sys
from itertools import combinations


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
possibles = []
alphabets = set()
for _ in range(n):
    word = set(list(input()))
    if len(word) > k:
        continue
    alphabets.update(word)
    possibles.append(word)


def solve(n, k, possibles, alphabets):
    if not possibles:
        return 0
    basic = {'a', 'n', 't', 'i', 'c'}
    alphabets = alphabets - basic
    k -= 5
    if k > len(alphabets):
        k = len(alphabets)
    answer = 0
    for teached in combinations(alphabets, k):
        teached = set(teached) | basic
        cnt = 0
        for word in possibles:
            if word.issubset(teached):
                cnt += 1
        answer = max(answer, cnt)
    return answer


print(solve(n, k, possibles, alphabets))
