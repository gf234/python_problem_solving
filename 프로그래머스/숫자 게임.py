import bisect


def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    score = 0
    for a in A:
        n = len(B)
        i = bisect.bisect_right(B, a)
        if i == n:
            B.pop(0)
        else:
            score += 1
            B.pop(i)
    return score
