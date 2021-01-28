def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        k = i - 1
        while k >= 0:
            if temp >= arr[k]:
                break
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = temp
    return arr


arr = [3, 5, 1, 4, 2]
print(insertionSort(arr))
