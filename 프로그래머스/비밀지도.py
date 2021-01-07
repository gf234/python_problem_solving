def solution(n, arr1, arr2):
    answer = []
    for code1, code2 in zip(arr1, arr2):
        row = bin(code1 | code2)[2:]
        row = row.rjust(n, ' ')
        row = row.replace('1', '#')
        row = row.replace('0', ' ')
        answer.append(row)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)
