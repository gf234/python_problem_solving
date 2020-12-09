from collections import defaultdict


def solution(str1, str2):
    def generate(str):
        ret = defaultdict(lambda: 0)
        for i in range(len(str)-1):
            a, b = str[i], str[i+1]
            if a.isalpha() and b.isalpha():
                c = (a+b).upper()
                ret[c] += 1
        return ret
    s1 = generate(str1)
    s2 = generate(str2)
    s = 0
    i = 0
    for k in s1:
        if k in s2:
            s += max(s1[k], s2[k])
            i += min(s1[k], s2[k])
        else:
            s += s1[k]
    for k in s2:
        if k not in s1:
            s += s2[k]

    if s == 0:
        j = 1
    else:
        j = i/s
    return int(j*65536)


str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))
