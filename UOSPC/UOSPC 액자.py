import sys
from collections import defaultdict

n = int(input())
s = input()
m = int(input())
t = input()

starts = []
if t[0] in s:
    for i, c in enumerate(s):
        if c == t[0]:
            starts.append(i)

ans = ''
for start in starts:
    i = 1
    ss = start+1
    flag = False
    for c in s[start+1:]:
        if i >= m:
            ans = 'YES'
            flag = True
            break
        if t[i] != c:
            break
        i += 1
        ss += 1
    i -= 1
    if flag:
        break
    subt = t[i+1:]
    if subt in s[ss:]:
        ans = 'YES'
        break
else:
    ans = 'NO'

print(ans)
