import bisect
import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

cards.sort()

ans = []
for x in nums:
    ans.append(bisect.bisect(cards, x) - bisect.bisect_left(cards, x))

for x in ans:
    print(x,end=" ")