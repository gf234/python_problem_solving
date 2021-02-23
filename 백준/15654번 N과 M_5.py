from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

permuts = permutations(nums, m)
for permut in permuts:
    print(' '.join(map(str, permut)))
