import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
arr = list(map(int, input().split()))
p, q = -1, -1
oneIndex = -1
for i in range(n):
    if arr[i] == 1:
        oneIndex = i
    next = arr[i]+1
    if next == n+1:
        next = 1
    before = arr[i]-1
    if before == 0:
        before = n

    ni = i+1
    if ni == n:
        ni = 0
    bi = i-1
    if bi == -1:
        bi = n-1
    if arr[bi] == before:
        if arr[ni] == next:
            continue
        p = ni
    if arr[ni] == next:
        q = bi

if p < q:
    c = n
elif p > q:
    c = n-p
    arr = arr[p:]+arr[:p]
    p = 0
    q = q+c
else:
    c = n-oneIndex-1
    if c == 0:
        c = n
    else:
        arr = arr[oneIndex+1:]+arr[:oneIndex+1]
    p = 0
    q = n-1

arr = arr[:p]+list(reversed(arr[p:q+1]))+arr[q+1:]
for i in range(n):
    if arr[i] == 1:
        print(n-i)
        print(p+1, q+1)
        print(c)
        break
