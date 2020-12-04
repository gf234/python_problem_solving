from itertools import permutations


def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    c = priority[n]
    return str(eval(c.join((calc(priority, n+1, e)for e in expression.split(c)))))


def solution(expression):
    answer = 0
    operator = ('*', '-', '+')
    priorities = permutations(operator, 3)
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer
