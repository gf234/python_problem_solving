

def solution(m, n, puddles):
    DIV = 1000000007

    board = [[0 for _ in range(m)]for _ in range(n)]
    for mm, nn in puddles:
        board[nn-1][mm-1] = 1

    cache = [[-1 for _ in range(101)]for _ in range(101)]
    dir = [[0, 1], [1, 0]]

    def recur(mm, nn):
        if mm == m-1 and nn == n-1:
            return 1

        if cache[mm][nn] != -1:
            return cache[mm][nn]

        ret = 0
        for dm, dn in dir:
            nextm = mm + dm
            nextn = nn + dn
            if not(nextm >=m or nextn >=n):
                if board[nextn][nextm]:
                    continue
                ret += recur(nextm, nextn)
        ret %= DIV
        cache[mm][nn] = ret
        return cache[mm][nn]
    answer = recur(0, 0)
    return answer

m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles))