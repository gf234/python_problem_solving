import sys
import math
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n = int(input())
expression = input()
numOps = n//2

# 0 1 2 3 4
#   0   1
answer = -math.inf


def recur(pos, brackets):
    global answer
    if pos >= numOps:
        q = deque(expression)
        i = 0
        temp = ""
        for bracket in brackets:
            while i != bracket:
                while True:
                    c = q.popleft()
                    temp += c
                    if not c.isnumeric():
                        break
                i += 1
            temp += '('
            for _ in range(3):
                temp += q.popleft()
            temp += ')'
            i += 1
        else:
            while q:
                temp += q.popleft()
        answer = max(answer, eval(temp))
        return

    recur(pos+1, brackets)
    brackets.append(pos)
    recur(pos+2, brackets)
    brackets.pop()


recur(0, [])
print(answer)
