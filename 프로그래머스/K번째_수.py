n = int(input())
k = int(input())


def bisec(start, end):
    mid = (start+end)//2

    if start > end:
        return start

    # mid이하인 수의 개수 구하기
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        return bisec(start, mid-1)
    else:
        return bisec(mid+1, end)


ans = bisec(1, k)

print(ans)
