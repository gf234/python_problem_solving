def solution(msg):
    dictNum = 1
    d = dict()
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in s:
        d[c] = dictNum
        dictNum += 1
    maxLen = 1
    ind = 0
    ans = []
    while True:
        prev = ind
        for l in range(min(len(msg)-ind, maxLen), 0, -1):
            if msg[ind:ind+l] in d:
                ans.append(d[msg[ind:ind+l]])
                ind += l
                break
        if ind >= len(msg):
            break
        else:
            maxLen = max(maxLen, ind+1-prev)
            d[msg[prev:ind+1]] = dictNum
            dictNum += 1
    return ans


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
