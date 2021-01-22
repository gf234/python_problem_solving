from collections import defaultdict


def solution(numbers, hand):
    d = dict()
    num = 1
    for i in range(3):
        for j in range(3):
            d[num] = (i, j)
            num += 1
    d['*'] = (3, 0)
    d[0] = (3, 1)
    d['#'] = (3, 2)

    def calDist(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    left = '*'
    right = '#'

    answer = ""
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left = number
        elif number in (3, 6, 9):
            answer += 'R'
            right = number
        elif number in (2, 5, 8, 0):
            lDist = calDist(d[left], d[number])
            rDist = calDist(d[right], d[number])

            if lDist < rDist:
                answer += 'L'
                left = number
            elif lDist > rDist:
                answer += 'R'
                right = number
            elif hand == 'left':
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
