def solution(n):
    decimals = [True for _ in range(n+1)]
    decimals[0] = False
    decimals[1] = False
    answer = 1

    for i in range(3, n+1, 2):
        if decimals[i]:
            answer += 1
            for j in range(i*2, n+1, i):
                decimals[j] = False
    return answer
