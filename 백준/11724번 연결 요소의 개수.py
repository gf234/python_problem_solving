import sys

n, m = map(int, input().split())

adj = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

visited = set()
answer = 0
for i in range(n):
    if i not in visited:
        answer += 1
        stack = []
        stack.append(i)

        while stack:
            here = stack.pop()
            visited.add(here)

            for there in adj[here]:
                if there not in visited:
                    stack.append(there)

print(answer)
