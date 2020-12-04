import sys
import math
from collections import defaultdict, deque

n, m, l = map(int, input().split())

confirmed = set(map(int, sys.stdin.readline().rstrip().split()))

# 접촉 정보
contact_infos = defaultdict(set)
for _ in range(l):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    contact_infos[a].add((b, c))
    contact_infos[b].add((a, c))

infection_time = defaultdict(lambda: -1)
for p in confirmed:
    infection_time[p] = math.inf

check = deque(confirmed)

# 새롭게 나온 확진자에 대해서 검사
while check:
    c = check.popleft()
    # 해당 확진자의 접촉 정보를 확인
    for contact, contact_t in contact_infos[c]:
        # 접촉 시간이 확진 시간 후
        if contact_t <= infection_time[c]:
            # 이미 접촉자인 경우에 더 이전에 접촉했으면 업데이트 해준다. 새롭게 나온 확진자에 추가.
            if infection_time[contact] < contact_t:
                infection_time[contact] = contact_t
                confirmed.add(contact)
                check.append(contact)

ans = sorted(list(confirmed))

for a in ans:
    print(a)
