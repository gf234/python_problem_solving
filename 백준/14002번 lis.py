n = int(input())
arr = list(map(int, input().split()))
# dp[i]: i에서 끝나는 LIS의 최대 길이
dp = [1 for _ in range(n)]
# lis[i]: i에서 끝나는 LIS 저장
lis = [[x] for x in arr]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j]+1:
                lis[i] = lis[j] + [arr[i]]
                dp[i] = dp[j]+1

length = -1
maxInd = -1
for i in range(n):
    if length < dp[i]:
        maxInd = i
        length = dp[i]

print(length)
print(*lis[maxInd])
