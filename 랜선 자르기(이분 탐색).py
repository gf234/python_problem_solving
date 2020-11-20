import bisect
import sys

k, n = map(int, input().split())

lengths = []
for _ in range(k):
    length = int(sys.stdin.readline().rstrip())
    lengths.append(length)

max_length = max(lengths)
min_length = max_length // n+1


def bisec(start, end):
    mid = (start+end)//2
    if start > end:
        return mid
    ret = mid

    sum = 0
    for length in lengths:
        sum += length // mid
    if sum < n:
        ret = bisec(start, mid-1)
    else:
        ret = bisec(mid+1, end)
    return ret


ans = bisec(min_length, max_length)

print(ans)
