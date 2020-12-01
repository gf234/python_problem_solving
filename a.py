from itertools import permutations


def solution(n, k):
    arr = [i for i in range(1, n+1)]
    permuts = list(permutations(arr, n))
    return list(permuts[n-1])
