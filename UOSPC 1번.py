s, t = input().split()


def convert(num, N):
    ret = 0
    for i, c in enumerate(num[::-1]):
        ret += int(c)*(N**i)
    return ret

smx = int(max(s))
tmx = int(max(t))

cnt = 0
a = []
b = []
for N in range(smx+1, 11):
    a.append(convert(s, N))

for N in range(tmx+1, 11):
    b.append(convert(t, N))

for N in a:
    for M in b:
        if N == M:
            cnt += 1

print(cnt)