import re


def solution(dartResult):
    # s, d, t: 1제곱, 2제곱, 3제곱, 점수마다 하나씩
    # *: 해당 점수, 바로 전 점수 2배
    # #: 해당 점수 마이너스
    # *, #은 둘 중 하나만 존재하거나 존재하지 않음
    before = 0
    answer = 0

    p = re.compile('(\d+)(\D+)')
    m = p.findall(dartResult)

    for current, info in m:
        current = int(current)

        for c in info:
            if c == 'D':
                current = current**2
            if c == 'T':
                current = current**3
            if c == '*':
                answer += before
                current *= 2
            if c == '#':
                current = -current
        answer += current
        before = current
    return answer


dartResult = input()
solution(dartResult)
