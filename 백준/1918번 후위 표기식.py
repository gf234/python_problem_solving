exp = '(' + input()+')'

priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}
stack = []
for c in exp:
    if 'A' <= c <= 'Z':
        print(c, end='')
    elif c == '(':
        stack.append(c)
    elif c == ')':
        top = stack.pop()
        while top != '(':
            print(top, end='')
            top = stack.pop()
    else:
        while stack and priority[c] <= priority[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(c)
print()
