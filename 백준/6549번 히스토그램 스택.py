import sys
import heapq

while True:
    n, *h = map(int, input().split())

    if n == 0:
        break

    stack = [0]
    answer = 0
    for i in range(1, n):
        while h[stack[-1]] > h[i]:
            top = h[stack.pop()]

            if stack:
                answer = max(answer, top*(i - stack[-1] - 1))
            else:
                answer = max(answer, top*i)
                break
        stack.append(i)
    else:
        i = n
        while stack:
            top = h[stack.pop()]

            if stack:
                answer = max(answer, top*(i - stack[-1] - 1))
            else:
                answer = max(answer, top*i)
                break
    print(answer)
