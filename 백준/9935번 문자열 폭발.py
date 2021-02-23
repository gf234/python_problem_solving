s = input()
exp = input()
l = len(exp)


def solve():
    if l == 1:
        answer = s.replace(exp, '')
        if answer:
            print(''.join(answer))
        else:
            print('FRULA')
        return

    answer = []
    stack = []
    pos = 0
    for c in s:
        answer.append(c)
        if c == exp[0]:
            stack.append(pos)
            pos = 1
            continue
        if c == exp[pos]:
            stack.append(pos)
            pos += 1
            if pos == l:
                for _ in range(l):
                    temp = stack.pop()
                    answer.pop()
                else:
                    pos = temp
        else:
            stack.clear()
            pos = 0

    if answer:
        print(''.join(answer))
    else:
        print('FRULA')


solve()
