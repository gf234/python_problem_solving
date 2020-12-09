def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1
        sl = len(s)
        zeros = s.count('0')
        answer[1] += zeros
        s = bin(sl - zeros)[2:]

    return answer


s = "110010101001"
print(solution(s))
