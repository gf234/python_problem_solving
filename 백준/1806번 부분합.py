import math
n, s = map(int, input().split())
arr = list(map(int, input().split()))


def solution(n, s, arr):
    answer = math.inf

    left = 0
    right = 0
    sum = arr[0]
    while True:
        if sum >= s:
            answer = min(answer, right-left+1)
            sum -= arr[left]
            left += 1
        else:
            right += 1
            if right >= n:
                break
            sum += arr[right]

    if answer == math.inf:
        print(0)
    else:
        print(answer)


solution(n, s, arr)
