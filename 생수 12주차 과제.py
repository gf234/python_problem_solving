n = 2
prev = 1
while True:
    cur = prev + str(n).count('1')
    if cur == n:
        print(f'답 : {n}')
        break
    n += 1
    prev = cur
