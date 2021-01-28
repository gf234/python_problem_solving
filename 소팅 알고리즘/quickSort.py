def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n//2]
    less = []
    more = []
    equal = []
    for a in arr:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
    return quickSort(less)+equal+quickSort(more)


arr = [3, 5, 1, 4, 2]
print(quickSort(arr))
