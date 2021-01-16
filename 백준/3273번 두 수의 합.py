from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

d = defaultdict(list)
for i, num in enumerate(arr):
    d[num].append(i)

answer = 0
for num in arr:
    if (k-num) in d:
        answer += len(d[k-num])

print(answer//2)
