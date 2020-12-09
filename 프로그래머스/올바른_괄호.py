def solution(s):
    lcnt = 0
    for c in s:
        if c == '(':
            lcnt += 1
        else:
            lcnt -= 1
        if lcnt < 0:
            return False
    if lcnt == 0:
        return True
    else:
        return False
