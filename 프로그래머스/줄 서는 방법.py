def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    cnt = factorial(n)

    while True:
        if n == 0:
            break

        cnt //= n
        now = (k-1)//cnt
        answer.append(arr[now])
        arr.pop(now)
        n -= 1
        k %= cnt
        if k == 0:
            k = cnt
    return answer
