import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
abcd = []
for _ in range(n):
    row = list(map(int, input().split()))
    abcd.append(row)

absum = dict()
for i in range(n):
    for j in range(n):
        ab = abcd[i][0]+abcd[j][1]
        absum[ab] = absum.get(ab, 0)+1

answer = 0
for i in range(n):
    for j in range(n):
        cd = -(abcd[i][2]+abcd[j][3])
        if cd in absum:
            answer += absum[cd]
print(answer)
