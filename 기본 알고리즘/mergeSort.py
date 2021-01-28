import sys


def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
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


arr = [3, 5, 1, 4, 2]
print(mergeSort(arr))
