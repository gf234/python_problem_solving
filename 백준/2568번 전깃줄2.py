import sys
import bisect


def input(): return sys.stdin.readline().rstrip()


n = int(input())
infos = []
for _ in range(n):
    a, b = map(int, input().split())
    infos.append((a, b))
infos.sort()

stack = [0]
backtrace = []
lis = 0
for a, b in infos:
    if stack[-1] < b:
        stack.append(b)
        lis += 1
        backtrace.append((lis, a))
    else:
        ind = bisect.bisect_left(stack, b)
        stack[ind] = b
        backtrace.append((ind, a))

pos = lis
lives = set()
while backtrace:
    ind, val = backtrace.pop()
    if ind == pos:
        pos -= 1
        lives.add(val)

print(n-lis)
for a, _ in infos:
    if a not in lives:
        print(a)
