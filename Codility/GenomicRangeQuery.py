# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    # S[:i] 까지 factor들의 등장 횟수
    factorCounters = [[0, 0, 0, 0]]
    for i, c in enumerate(S):
        prev = list(factorCounters[i])
        if c == 'A':
            prev[0] += 1
        if c == 'C':
            prev[1] += 1
        if c == 'G':
            prev[2] += 1
        if c == 'T':
            prev[3] += 1
        factorCounters.append(prev)

    answer = []
    for i in range(len(P)):
        a = P[i]
        b = Q[i]+1

        for j in range(4):
            if factorCounters[b][j] - factorCounters[a][j] > 0:
                answer.append(j+1)
                break
        else:
            answer.append(0)
    return answer


S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))
