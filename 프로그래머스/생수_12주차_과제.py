# n = 2일때 부터 시작, 이전 값인 f(1)을 prev에 저장
n = 2
prev = 1
# cur = f(n)
# prev = f(n-1)
while True:
    # int형인 n을 string으로 변환하여 
    # 각 자리수에서 1의 개수를 센후 f(n-1)에 더한다.
    cur = prev + str(n).count('1')
    # f(n) = n인 2번째 값이 나오면 값을 print하고 끝낸다.
    if cur == n:
        print(f'f(n) = n인 2번째 양수 : {n}')
        break
    n += 1
    prev = cur
