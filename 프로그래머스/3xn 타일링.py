def solution(n):
    f = [0 for _ in range(n+1)]
    f[0] = 1
    prev_sum = 0
    for i in range(2, n+1, 2):
        f[i] = f[i-2]*3+prev_sum*2
        prev_sum += f[i-2]
    answer = f[n] % 1000000007
    return answer
