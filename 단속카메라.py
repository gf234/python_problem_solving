def solution(routes):
    routes.sort(key=lambda x: x[1])
    n = len(routes)
    lastCmeara = -30001
    cnt = 0

    for a, b in routes:
        if lastCmeara < a:
            cnt += 1
            lastCmeara = b

    return cnt


