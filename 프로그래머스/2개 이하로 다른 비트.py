def solution(numbers):
    answer = []
    for number in numbers:
        bit = 1
        while True:
            if bit & number == 0:
                if bit == 1:
                    answer.append(number | bit)
                else:
                    answer.append((number | bit) ^ (bit >> 1))
                break
            bit <<= 1

    return answer


numbers = [2, 7]
print(solution(numbers))
