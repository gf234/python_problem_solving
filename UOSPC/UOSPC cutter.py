import sys
from collections import Counter, defaultdict
n = int(input())
colors = list(map(int, input().split()))

adj = [set()for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    adj[a].add(b)
    adj[b].add(a)


def find_leaf():
    leaf = []
    for i in range(n):
        if len(adj[i]) == 1:
            leaf.append(i)
    return leaf


while True:
    flag = True
    leafs = find_leaf()

    deletes = []
    leaf_colors = defaultdict(set)
    for leaf in leafs:
        leaf_colors[colors[leaf]].add(leaf)
        if len(leaf_colors[colors[leaf]]) == 2:
            deletes.extend(leaf_colors[colors[leaf]])
            flag = False

    for here in deletes:
        for there in adj[here]:
            adj[there].remove(here)
        adj[here].clear()
    if flag:
        break

ans = []
for i in range(n):
    if len(adj[i]) >= 1:
        ans.append(i)

ans.sort()
print(len(ans))
for a in ans:
    print(a+1, end=' ')
