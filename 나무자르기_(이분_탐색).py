n, m = map(int, input().split())

heights = list(map(int, input().split()))

max_heights = max(heights)
min_heights = 0

ans = 0


def bisec(start, end):
    if start > end:
        return

    mid = (start+end) // 2
    global ans

    hsum = 0
    for height in heights:
        if height > mid:
            hsum += height - mid

    if hsum < m:
        bisec(start, mid-1)
    else:
        ans = mid
        bisec(mid+1, end)


bisec(min_heights, max_heights)

print(ans)
