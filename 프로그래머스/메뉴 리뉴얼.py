from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for count in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), count)
        most_ordered = Counter(order_combinations).most_common()
        answer += [''.join(k) for k, v in most_ordered if v >=
                   2 and v == most_ordered[0][1]]
    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
