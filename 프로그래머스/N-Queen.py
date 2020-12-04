def recur(n, pos, choosed):
    if pos == n:
        return 1

    ret = 0
    for i in range(n):
        if i not in choosed:
            for j in range(pos):
                if abs(choosed[j]-i) == pos-j:
                    break
            else:
                choosed.append(i)
                ret += recur(n, pos+1, choosed)
                choosed.pop()
    return ret


def solution(n):
    return recur(n, 0, list())
