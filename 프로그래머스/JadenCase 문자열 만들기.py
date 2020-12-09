def solution(s):
    jadencase = []
    words = s.split()
    for word in words:
        temp = word.lower()
        if temp[0].isalpha():
            jadencase.append(temp[0].upper() + temp[1:])
        else:
            jadencase.append(temp)
    ans = ''
    i = 0
    flag = True
    for c in s:
        if c == ' ':
            ans += c
            flag = True
        elif flag:
            ans += jadencase[i]
            i += 1
            flag = False
    return ans
