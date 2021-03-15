import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

asum = [A[0]]
bsum = [B[0]]
for i in range(1, n):
    asum.append(asum[-1]+A[i])
for i in range(1, m):
    bsum.append(bsum[-1]+B[i])

temp = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        sum = asum[j] if i == 0 else asum[j]-asum[i-1]
        temp[sum] += 1

answer = 0
for i in range(m):
    for j in range(i, m):
        sum = bsum[j] if i == 0 else bsum[j]-bsum[i-1]
        if (t-sum) in temp:
            answer += temp[t-sum]
print(answer)
