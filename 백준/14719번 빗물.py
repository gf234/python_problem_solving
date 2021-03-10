import sys


def input(): return sys.stdin.readline().rstrip()


h, w = map(int, input().split())
heights = list(map(int, input().split()))


def solve(h, w, heights):
    if w < 3:
        return 0

    top = heights[0]
    stack = []
    answer = 0
    for i in range(1, w-1):
        if top > heights[i]:
            stack.append(heights[i])
        else:
            while stack:
                answer += top - stack.pop()
            top = heights[i]
    else:
        left = top
        h = min(left, heights[-1])
        while stack:
            temp = stack.pop()
            if temp < h:
                answer += h - temp
            else:
                h = min(left, temp)
    return answer


print(solve(h, w, heights))
