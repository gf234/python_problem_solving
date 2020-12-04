from itertools import combinations


def solution(nums):
    ans = 0

    prime_number = [True if i % 2 == 1 else False for i in range(3000)]
    prime_number[1] = False
    prime_number[2] = True
    for i in range(3, 3000, 2):
        if prime_number[i]:
            for j in range(i*2, 3000, i):
                prime_number[j] = False

    combs = combinations(nums, 3)
    for comb in combs:
        s = sum(comb)
        if prime_number[s]:
            ans += 1
    return ans
