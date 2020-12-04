import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

n = int(input())

if n == 0:
    sys.exit(0)

water_tanks = [(-1, -1)]
for _ in range(n):
    s, h = map(int, sys.stdin.readline().rstrip().split())
    water_tanks.append((s, h))

parents = defaultdict(lambda: 0)
childs = defaultdict(list)
for _ in range(n-1):
    u, v, h = map(int, sys.stdin.readline().rstrip().split())
    childs[u].append((h, v))
    childs[u].sort()
    parents[v] = u

if n == 1:
    s, h = water_tanks[1]
    print(s*h)
    sys.exit(0)

# 말단 : 차오르기 시작하는 시간 + 부피
# 중간 : 차오르기 시작하는 시간 + 자식들의 부피 + 부피
# 시작 : 자식들의 부피 + 부피
ans = [0 for _ in range(n+1)]


def find_t(num, prev_t, prev_h):
    sn, hn = water_tanks[num]
    # 말단
    if not childs[num]:
        return prev_t + (sn*hn)

    # 중간
    for h, v in childs[num]:
        prev_t += (h-prev_h)*sn
        ans[v] = find_t(v, prev_t, 0)
        prev_t = ans[v]
        prev_h = h
    else:
        ans[num] = (hn-prev_h)*sn + prev_t
    return ans[num]




find_t(1, 0, 0)

for i in range(1, n+1):
    print(ans[i])
