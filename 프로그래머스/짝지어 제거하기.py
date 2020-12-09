def solution(s):
    stack = [-1]
    for c in s:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 1:
        return 1
    else:
        return 0
