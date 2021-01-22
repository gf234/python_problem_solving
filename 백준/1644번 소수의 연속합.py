import sys

n = int(input())


def solution(n):
    if n == 1:
        print(0)
        return

    isDecimal = [False if i % 2 == 0 else True for i in range(n+1)]
    isDecimal[0] = False
    isDecimal[1] = False
    isDecimal[2] = True
    decimal = [2]

    for i in range(3, n+1):
        if isDecimal[i]:
            decimal.append(i)
            for j in range(i*2, n+1, i):
                isDecimal[j] = False

    start = 0
    end = 0
    summ = decimal[0]

    answer = 0
    while True:
        if summ == n:
            answer += 1
            summ -= decimal[start]
            start += 1
            end += 1
            if end >= len(decimal):
                break
            summ += decimal[end]
        elif summ < n:
            end += 1
            if end >= len(decimal):
                break
            summ += decimal[end]
        else:
            summ -= decimal[start]
            start += 1
    print(answer)


solution(n)
