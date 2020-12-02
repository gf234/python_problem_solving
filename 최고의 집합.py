def solution(n, s):
    mid = s//n
    if mid == 0:
        return [-1]
    lack = s - mid*n
    answer = [mid for _ in range(n)]
    if lack == 0:
        return answer
    else:
        for i in range(lack):
            answer[i % n] += 1
        answer.sort()
        return answer