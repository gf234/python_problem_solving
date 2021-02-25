import sys


def input(): return sys.stdin.readline().rstrip()


mat = []
zeros = []
for i in range(9):
    row = list(map(int, list(input())))
    for j in range(9):
        if row[j] == 0:
            zeros.append((i, j))
    mat.append(row)
zeroNum = len(zeros)


def find_possibles(i, j):
    possibles = set([x for x in range(1, 10)])
    for y in range(9):
        if mat[i][y] in possibles:
            possibles.remove(mat[i][y])
    for x in range(9):
        if mat[x][j] in possibles:
            possibles.remove(mat[x][j])

    dx = (i//3)*3
    dy = (j//3)*3
    for x in range(3):
        for y in range(3):
            if mat[x+dx][y+dy] in possibles:
                possibles.remove(mat[x+dx][y+dy])
    return sorted(possibles)


def recur(ind):
    if ind == zeroNum:
        for row in mat:
            print(''.join(map(str, row)))
        return True
    i, j = zeros[ind]
    possibles = find_possibles(i, j)
    for x in possibles:
        mat[i][j] = x
        if recur(ind+1):
            return True
    mat[i][j] = 0
    return False


recur(0)
