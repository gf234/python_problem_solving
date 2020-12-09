def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    answer = [[0 for _ in range(m)]for _ in range(n)]

    for x in range(n):
        for y in range(m):
            sum = 0
            for i in range(len(arr1[0])):
                sum += arr1[x][i]*arr2[i][y]
            answer[x][y] = sum
    return answer
