import math


def solution(n, stations, w):
    answer = 0
    prev = 1
    for station in stations:
        start = max(1, station - w)
        end = min(n, station + w)

        if prev < start:
            answer += math.ceil((start - prev) / (w*2+1))
        prev = end+1
    else:
        if prev <= n:
            answer += math.ceil((n + 1 - prev) / (w*2+1))
    return answer


while True:
    n = int(input())
    if n == -1:
        break
    stations = list(map(int, input().split()))
    w = int(input())
    print(solution(n, stations, w))
