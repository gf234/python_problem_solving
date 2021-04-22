import sys


def input(): return sys.stdin.readline().rstrip()


g = int(input())
p = int(input())
planes = []
for _ in range(p):
    planes.append(int(input()))

parent = [i for i in range(g+1)]


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return


answer = 0
for x in planes:
    next = find(x)
    if next == 0:
        break
    answer += 1
    union(next-1, x)
print(answer)
