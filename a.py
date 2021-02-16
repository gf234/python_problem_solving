from collections import deque
import sys

t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    def d(n):
        n *= 2
        if n > 9999:
            n = n % 10000
        return n

    def s(n):
        if n == 0:
            n = 9999
        else:
            n -= 1
        return n

    def l(n):
        s = str(n)
        if len(s) < 4:
            s = '0'*(4-len(s)) + s
        n = int(s[1]+s[2]+s[3]+s[0])
        return n

    def r(n):
        s = str(n)
        if len(s) < 4:
            s = '0'*(4-len(s)) + s
        n = int(s[3]+s[0]+s[1]+s[2])
        return n

    q = deque()
    q.append(a)
    commands = dict()
    commands[a] = ''
    answer = ''
    while q:
        here = q.popleft()
        if here == b:
            answer = commands[here]
            break

        temp = d(here)
        if temp not in commands:
            q.append(temp)
            commands[temp] = commands[here] + 'D'

        temp = s(here)
        if temp not in commands:
            q.append(temp)
            commands[temp] = commands[here] + 'S'

        temp = l(here)
        if temp not in commands:
            q.append(temp)
            commands[temp] = commands[here] + 'L'

        temp = r(here)
        if temp not in commands:
            q.append(temp)
            commands[temp] = commands[here] + 'R'

    print(answer)
