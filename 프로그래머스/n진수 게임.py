def solution(n, t, m, p):
    p -= 1
    num = 0
    order = 0
    ans = ""

    def convert(num):
        T = '0123456789ABCDEF'
        quot, remain = divmod(num, n)
        if quot == 0:
            return T[remain]
        else:
            return convert(quot) + T[remain]
    numstr = convert(num)
    ind = 0
    while len(ans) != t:
        if order % m == p:
            ans += numstr[ind]
        ind += 1
        if ind == len(numstr):
            num += 1
            numstr = convert(num)
            ind = 0
        order += 1
    return ans


n = 2
t = 4
m = 2
p = 1
print(solution(n, t, m, p))
