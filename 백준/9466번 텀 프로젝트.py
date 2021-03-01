import sys


def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    wants = [0] + list(map(int, input().split()))

    answer = n
    visited = set()

    def dfs(start):
        stack = []
        stack.append(start)
        count = 1
        temp = dict()
        temp[start] = count
        while stack:
            here = stack.pop()
            there = wants[here]
            if there not in visited:
                count += 1
                temp[there] = count
                visited.add(there)
                stack.append(there)
            elif there in temp:
                return count - temp[there] + 1
        return 0

    for i in range(1, n+1):
        if i not in visited:
            sub = dfs(i)
            answer -= sub
    print(answer)
