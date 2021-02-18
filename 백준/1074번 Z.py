n, r, c = map(int, input().split())

answer = 0
while n:
    mid = 2**(n-1)
    sum = 4**(n-1)
    if r < mid:
        if c < mid:
            pass
        else:
            c -= mid
            answer += sum
    else:
        if c < mid:
            r -= mid
            answer += sum*2
        else:
            r -= mid
            c -= mid
            answer += sum*3
    n -= 1
print(answer)
