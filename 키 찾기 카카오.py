def rotate90(key):
    ret = []
    for j in range(len(key)):
        temp = []
        for i in range(len(key)-1, -1, -1):
            temp.append(key[i][j])
        ret.append(temp)
    return ret


def check(key, lock):
    n = len(key)*2+len(lock)-2
    board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(key)+len(lock)-1):
        for j in range(len(key)+len(lock)-1):
            for x in range(len(lock)):
                for y in range(len(lock)):
                    board[x+len(key)-1][y+len(key)-1] = lock[x][y]
            for x in range(len(key)):
                for y in range(len(key)):
                    board[x+i][y+j] += key[x][y]

            for x in range(len(lock)):
                notFit = False
                for y in range(len(lock)):
                    if board[x+len(key)-1][y+len(key)-1] != 1:
                        notFit = True
                        break
                if notFit:
                    break
            else:
                return True
    return False


def solution(key, lock):
    answer = True

    if len(key) == 1:
        cnt = 0
        for i in range(len(lock)):
            for j in range(len(lock)):
                if lock[i][j] == 0:
                    cnt += 1
                if cnt > 2:
                    return False
        return True

    answer = check(key, lock)
    if answer:
        return answer
    for _ in range(3):
        key = rotate90(key)
        answer = check(key, lock)
        if answer:
            return answer
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
