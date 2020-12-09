def check(arr):
    n = len(arr)

    a = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != a:
                return False
    return True


answer = [0, 0]


def quad(arr):
    if check(arr):
        answer[arr[0][0]] += 1
        return

    n = len(arr)//2
    subs = []
    subs.append([row[:n] for row in arr[:n]])
    subs.append([row[n:] for row in arr[:n]])
    subs.append([row[:n] for row in arr[n:]])
    subs.append([row[n:] for row in arr[n:]])
    for sub in subs:
        quad(sub)
    return


def solution(arr):
    quad(arr)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution(arr))
