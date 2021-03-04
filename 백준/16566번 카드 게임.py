import sys
import math


def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())

cards = list(map(int, input().split()))
targets = list(map(int, input().split()))

sqrt_n = int(math.sqrt(n))
isPresence = [False for _ in range(n+1)]
# sqrt_n 개씩 잘라서 남은 개수를 저장한다.
dummy = [0 for _ in range(sqrt_n+1)]

for card in cards:
    isPresence[card] = True
    dummy[card // sqrt_n] += 1

for target in targets:
    minimum = target + 1
    # minimum이 불가능하면 다음 더미를 검사하여 가능한 값이 있는 더미로 변경해준다.
    while dummy[minimum // sqrt_n] == 0 and minimum <= n:
        minimum = ((minimum//sqrt_n) + 1) * sqrt_n

    while True:
        if isPresence[minimum]:
            isPresence[minimum] = False
            dummy[minimum//sqrt_n] -= 1
            print(minimum)
            break
        minimum += 1
