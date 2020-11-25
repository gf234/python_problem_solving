def solution(s):
    answer = []

    s = s[1:-1]

    lind = []
    rind = []
    for i, c in enumerate(s):
        if c == '{':
            lind.append(i)
        elif c == '}':
            rind.append(i)

    sets = []
    for i in range(len(lind)):
        sets.append(set(map(int, s[lind[i]+1:rind[i]].split(','))))
    sets.sort(key=lambda x: len(x))

    prev = set()
    for s in sets:
        answer.extend(s - prev)
        prev = s
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
