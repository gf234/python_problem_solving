from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    att = [i for i in range(col)]
    l = 1
    ans = []
    debug = []
    while l <= col:
        combs = combinations(att, l)
        for comb in combs:
            s = set()
            # 유일성 확인
            for i in range(row):
                temp = []
                for j in comb:
                    temp.append(relation[i][j])
                if tuple(temp) in s:
                    break
                s.add(tuple(temp))
            else:
                debug.append(set(comb))
                # 최소성 확인
                for a in ans:
                    if a.issubset(set(comb)):
                        break
                else:
                    ans.append(set(comb))
        l += 1
    return len(ans)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(relation))
