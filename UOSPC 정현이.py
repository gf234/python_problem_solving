from collections import deque

n = int(input())
cards = deque(map(int, input().split()))

sum = 0
while cards:
   a = [cards[0]+cards[1], cards[-1]+cards[-2], cards[0]+cards[-1]]
   maxInd = 0
   for i in range(1, 3):
       if a[i] > a[maxInd]: