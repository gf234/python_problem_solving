# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    lastMaxCounter = 0
    maxCount = 0
    counter = [0 for _ in range(N+1)]
    for x in A:
        if x <= N:
            if counter[x] >= lastMaxCounter:
                counter[x] += 1
                maxCount = max(maxCount, counter[x])
            else:
                counter[x] = lastMaxCounter+1
                maxCount = max(maxCount, counter[x])
        else:
            lastMaxCounter = maxCount

    for i in range(1, N+1):
        if counter[i] < lastMaxCounter:
            counter[i] = lastMaxCounter
    return counter[1:]
