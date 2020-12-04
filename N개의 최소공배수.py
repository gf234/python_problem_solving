import math


def solution(arr):
    if len(arr) == 1:
        return arr[0]

    gcd = math.gcd(arr[0], arr[1])
    lcm = arr[0]*arr[1] // gcd
    for x in arr[2:]:
        gcd = math.gcd(lcm, x)
        lcm = lcm*x // gcd
    return lcm
