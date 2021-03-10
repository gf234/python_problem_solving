n = int(input())
nums = list(map(int, input().split()))


def solve():
    if n == 1:
        return 'A'
    if n == 2:
        if nums[0] == nums[1]:
            return nums[0]
        return 'A'

    if nums[1] == nums[0]:
        a = 0
        b = nums[1]
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        b = nums[1] - nums[0]*a

    for i in range(n-1):
        if nums[i]*a+b != nums[i+1]:
            break
    else:
        return nums[-1]*a+b
    return 'B'


print(solve())
