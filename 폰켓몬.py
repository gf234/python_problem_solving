from collections import Counter
from itertools import combinations


def solution(nums):
    choose_num = len(nums)//2
    counter = Counter(nums)
    diff_num = len(counter)
    if choose_num <= diff_num:
        ans = choose_num
    else:
        ans = diff_num
    return ans


nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
