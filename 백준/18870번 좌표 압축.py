import bisect
n = int(input())

nums = list(map(int, input().split()))
sortedNums = sorted(set(nums))

answer = []
for num in nums:
    i = bisect.bisect_left(sortedNums, num)
    answer.append(str(i))

print(" ".join(answer))
