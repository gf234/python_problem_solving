def solution(d, budget):
    d.sort()

    answer = 0

    for cost in d:
        if budget >= cost:
            answer += 1
            budget -= cost
        else:
            break
    return answer
