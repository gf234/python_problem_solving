import bisect
import math

n = int(input())
infos = list(map(int, input().split()))
infos.sort()

minimum = math.inf
answer = None

for i in range(n-2):
    left = i + 1
    right = n-1
    while left < right:
        temp = infos[i]+infos[left]+infos[right]
        if minimum > abs(temp):
            minimum = abs(temp)
            answer = (infos[i], infos[left], infos[right])
        if temp == 0:
            break
        if temp > 0:
            right -= 1
        else:
            left += 1

print(' '.join(map(str, answer)))
