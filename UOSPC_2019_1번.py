b = int(input())
n = int(input())

costs = list(map(int, input().split()))

if b - sum(costs) >= 40:
    print("possible")
else:
    print("impossible")