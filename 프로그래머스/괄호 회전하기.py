from collections import deque


def is_correct_bracket(s):
    stack = []
    open = {'(', '[', '{'}
    for x in s:
        if x in open:
            stack.append(x)
        else:
            if not stack:
                return False
            temp = stack.pop()
            if (
                (temp == '(' and x != ')') or
                (temp == '[' and x != ']') or
                (temp == '{' and x != '}')
            ):
                return False
    if stack:
        return False
    return True


def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        if is_correct_bracket(s):
            answer += 1
        s.append(s.popleft())
    return answer
