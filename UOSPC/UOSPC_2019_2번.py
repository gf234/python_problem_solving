import sys
n, m = map(int, input().split())

ratings = []
for _ in range(m):
    r = list(map(int, sys.stdin.readline().rstrip().split()))
    ratings.append(r)


def max_point(user):
    arr = []

    for a, b in zip(ratings[user][:-1], ratings[user][1:]):
        if a < b:
            arr.append((a+1, 10))
            arr.append((b, -10))
    arr.sort()
    ret = 0
    sum = 0
    for _, point in arr:
        sum += point
        if sum > ret:
            ret = sum
    return ret


answer = 0

for i in range(m):
    answer += max_point(i)

print(answer)
