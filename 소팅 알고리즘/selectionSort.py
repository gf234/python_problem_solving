def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        jMin = i
        for j in range(i+1, n):
            if arr[j] < arr[jMin]:
                jMin = j
        if jMin != i:
            arr[i], arr[jMin] = arr[jMin], arr[i]
    return arr


arr = [3, 5, 1, 4, 2]
print(selectionSort(arr))
