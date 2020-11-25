import sys
n, c = map(int, input().split())

positions = []
for _ in range(n):
    positions.append(int(sys.stdin.readline().rstrip()))

positions.sort()

min_dist = 1
max_dist = max(positions) - min(positions)


# 최대 거리를 탐색한다.
def bisec(start, end):
    mid = (start+end) // 2

    if start > end:
        return mid

    # 현재 거리로 c이상의 개수를 놓을 수 있는지 판단
    count = 1
    cur = positions[0]
    for i in range(1, n):
        if positions[i] - cur >= mid:
            count += 1
            cur = positions[i]

    if count >= c:
        return bisec(mid+1, end)
    else:
        return bisec(start, mid-1)


ans = bisec(min_dist, max_dist)

print(ans)
