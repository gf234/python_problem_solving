import heapq
import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
gems = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))
bags = []
for _ in range(k):
    c = int(input())
    heapq.heappush(bags, c)

answer = 0
possibleGems = []
# 작은 가방부터 탐색한다.
while bags:
    bag = heapq.heappop(bags)
    # 보석들 중 가방안에 들어갈 수 있는 것들을 고른다.
    while gems and bag >= gems[0][0]:
        m, v = heapq.heappop(gems)
        heapq.heappush(possibleGems, -v)
    # 가능한 보석이 있으면 value가 가장 높은것을 넣는다.
    if possibleGems:
        answer -= heapq.heappop(possibleGems)
    # 가능한 보석이 없고 남은 보석도 없으면 종료한다.
    elif not gems:
        break

print(answer)
