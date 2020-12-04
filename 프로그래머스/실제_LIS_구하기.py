import bisect
import math
n = int(input())
A = list(map(int, input().split()))

stack = [-math.inf]
backtrace = []
lis = 0
for a in A:
    # 마지막 원소보다 크면 삽입
    if stack[-1] < a:
        stack.append(a)
        lis += 1
        backtrace.append((lis, a))
    else:
        ind = bisect.bisect_left(stack, a)
        stack[ind] = a
        backtrace.append((ind, a))

print(lis)

pos = lis
ans = []
while backtrace:
    ind, val = backtrace.pop()
    if ind == pos:
        pos -= 1
        ans.append(val)

ans.reverse()

for x in ans:
    print(x, end=" ")
