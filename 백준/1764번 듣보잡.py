n, m = map(int, input().split())

pSet = set()
for _ in range(n):
    name = input()
    pSet.add(name)

answer = []
for _ in range(m):
    name = input()
    if name in pSet:
        answer.append(name)
answer.sort()
print(len(answer))
print("\n".join(answer))
