import math
import bisect

n = int(input())
nums = list(map(int, input().split()))

stack = [-math.inf]
backtrack = []
lis = 0
for num in nums:
    if stack[-1] < num:
        lis += 1
        stack.append(num)
        backtrack.append((num, lis))
    else:
        ind = bisect.bisect_left(stack, num)
        stack[ind] = num
        backtrack.append((num, ind))

pos = lis
answer = []
while backtrack:
    num, ind = backtrack.pop()
    if ind == pos:
        answer.append(num)
        pos -= 1

answer.reverse()
print(lis)
print(' '.join(map(str, answer)))
