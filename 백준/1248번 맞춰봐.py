import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
s = input()

mat = [[-1 for _ in range(n)] for _ in range(n)]
ind = 0
for i in range(n):
    for j in range(i, n):
        mat[i][j] = s[ind]
        ind += 1

answer = []


def check(j, x):
    sum = x
    for i in range(j-1, -1, -1):
        sum += answer[i]
        if mat[i][j] == '0' and sum != 0:
            return False
        if mat[i][j] == '+' and sum <= 0:
            return False
        if mat[i][j] == '-' and sum >= 0:
            return False
    return True


def backtrack(pos):
    if pos == n:
        return True
    if mat[pos][pos] == '0':
        answer.append(0)
        if backtrack(pos+1):
            return True
        answer.pop()
    else:
        sign = 1 if mat[pos][pos] == '+' else -1
        for x in range(1, 11):
            x *= sign
            if check(pos, x):
                answer.append(x)
                if backtrack(pos+1):
                    return True
                answer.pop()
    return False


backtrack(0)
print(' '.join(map(str, answer)))
