def solution(n, arr1, arr2):
    def convert(arr):
        map = [[0 for _ in range(n)] for _ in range(n)]

        for i, code in enumerate(arr):
            binStr = bin(code)[2:]
            strLen = len(binStr)

            for j in range(strLen):
                if binStr[j] == '1':
                    map[i][n-strLen+j] = 1
        return map

    map1 = convert(arr1)
    map2 = convert(arr2)

    answer = []

    for i in range(n):
        row = ""
        for j in range(n):
            if map1[i][j] or map2[i][j]:
                row += '#'
            else:
                row += ' '
        answer.append(row)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)
