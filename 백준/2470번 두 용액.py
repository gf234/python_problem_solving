import math

n = int(input())
arr = list(map(int, input().split()))
arr.sort()


def solution(n, arr):
    # 모두 양수인 경우
    if arr[0] >= 0:
        print(arr[0], arr[1])
        return
    # 모두 음수인 경우
    if arr[-1] <= 0:
        print(arr[-2], arr[-1])
        return
    left = 0
    right = n-1
    answer = (arr[0]+arr[-1], (arr[0], arr[-1]))

    while left < right:
        temp = arr[left]+arr[right]
        if abs(temp) < abs(answer[0]):
            answer = (temp, (arr[left], arr[right]))
        if temp == 0:
            print(arr[left], arr[right])
            return
        if temp < 0:
            left += 1
        else:
            right -= 1
    print(answer[1][0], answer[1][1])


solution(n, arr)
