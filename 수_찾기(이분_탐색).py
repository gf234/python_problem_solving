import bisect
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
M = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()

for x in M:
    if bisect.bisect_left(A, x) != bisect.bisect(A, x):
        print(1)
    else:
        print(0)
