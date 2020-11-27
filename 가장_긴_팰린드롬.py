def solution(s):
    l = len(s)
    for n in range(l, 0, -1):
        for i in range(l-n+1):
            substr=s[i:i+n]
            if substr == substr[::-1]:
                return n
    return 0
