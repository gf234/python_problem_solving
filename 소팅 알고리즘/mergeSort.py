import sys


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)


def merge(left, right):
    ret = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            ret.append(left[leftIndex])
            leftIndex += 1
        else:
            ret.append(right[rightIndex])
            rightIndex += 1
    if leftIndex == len(left):
        ret.extend(right[rightIndex:])
    else:
        ret.extend(left[leftIndex:])
    return ret


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = mergeSort(arr)

for x in arr:
    print(x)
