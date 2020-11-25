import sys

M = int(input())

bit_set = 0b0

for _ in range(M):
    args = sys.stdin.readline().rstrip().split()

    op = args[0]
    num = 0
    if len(args) == 2:
        num = int(args[1])

    if op == "add":
        bit_set = bit_set | (1 << num)
    elif op == "remove":
        bit_set = bit_set & ~(1 << num)
    elif op == "check":
        if (bit_set & (1 << num)) == 0:
            print(0)
        else:
            print(1)
    elif op == "toggle":
        bit_set = bit_set ^ (1 << num)
    elif op == "all":
        bit_set = (1 << 21) - 1
    elif op == "empty":
        bit_set = 0
