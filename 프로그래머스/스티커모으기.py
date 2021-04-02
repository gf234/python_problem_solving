def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)

    useFirst = [0 for _ in range(n)]
    useSecond = [0 for _ in range(n)]
    useFirst[0] = useFirst[1] = sticker[0]
    useSecond[0] = 0
    useSecond[1] = sticker[1]

    for i in range(2, n-1):
        useFirst[i] = max(useFirst[i-2]+sticker[i], useFirst[i-1])
    for i in range(2, n):
        useSecond[i] = max(useSecond[i-2]+sticker[i], useSecond[i-1])
    return max(useFirst[-2], useSecond[-1])


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))
