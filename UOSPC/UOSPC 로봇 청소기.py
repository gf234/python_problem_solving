import sys

r, c = map(int, input().split())

board = [[1 for _ in range(c+2)] for _ in range(r + 2)]

robot = ()
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 동서남북, 0123
for i in range(1, r+1):
    cs = list(sys.stdin.readline().rstrip())
    for j, c in enumerate(cs, 1):
        if c == '.':
            board[i][j] = 0
        if c == 'S':
            robot = (i, j, 3)
        if c == 'D':
            board[i][j] = -1


def cond(c):
    if c == 'E':
        pass
    if c == 'W':
        pass
    if c == 'S':
        pass
    if c == 'N':
        pass


code = input()

for c in code:
    if c == 'L':
        pass
    if c == 'R':
        pass
    if c == 'G':
        pass

    if c == 'i':
        pass

    if c == 'w':
        pass

    if c == 'u':
        pass
