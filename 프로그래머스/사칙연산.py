import math

def solution(arr):
    dp_max = [[-math.inf for _ in range(101)] for _ in range(101)]
    dp_min = [[math.inf for _ in range(101)] for _ in range(101)]
    n = len(arr)//2 + 1

    for i in range(n):
        dp_max[i][i] = int(arr[i*2])
        dp_min[i][i] = int(arr[i*2])

    for l in range(1, n):
        for i in range(n-l):
            j = i+l
            for k in range(i, j):
                if arr[k*2+1] == '+':
                    dp_max[i][j] = max(dp_max[i][k]+dp_max[k+1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][k]+dp_min[k+1][j], dp_min[i][j])
                else:
                    dp_max[i][j] = max(dp_max[i][k]-dp_min[k+1][j], dp_max[i][j])
                    dp_min[i][j] = min(dp_min[i][k]-dp_min[k+1][j], dp_min[i][j])

    answer=dp_max[0][n-1]
    return answer