import sys


def input(): return sys.stdin.readline().rstrip()


R, C, m = map(int, input().split())
sharks = dict()
dir = (None, (-1, 0), (1, 0), (0, 1), (0, -1))
for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    # 속력이 너무 크면 쓸모없는 반복을 하게되므로 같은 칸에 도착하는 속력으로 조정해준다.
    if d == 1 or d == 2:
        s = s % ((R-1)*2)
    else:
        s = s % ((C-1)*2)
    sharks[(r, c)] = (s, d, z)


def converse(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3


def moveshark():
    temp = dict()
    for (r, c), (s, d, z) in sharks.items():
        nr, nc = r, c
        t = s
        while t:
            if (d == 1 and nr == 1) or (d == 2 and nr == R) or (d == 3 and nc == C) or (d == 4 and nc == 1):
                d = converse(d)
            dr, dc = dir[d]
            nr += dr
            nc += dc
            t -= 1
        if (nr, nc) in temp:
            shark = temp[(nr, nc)]
            if shark[2] < z:
                temp[(nr, nc)] = (s, d, z)
        else:
            temp[(nr, nc)] = (s, d, z)
    return temp


pos = 0
answer = 0
while pos < C:
    pos += 1
    for i in range(1, R+1):
        if (i, pos) in sharks:
            shark = sharks.pop((i, pos))
            answer += shark[2]
            break
    sharks = moveshark()
print(answer)
