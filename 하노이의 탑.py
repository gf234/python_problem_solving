def solution(n):
    def hanoi(n, here, there, ans):
        if n == 1:
            ans.append([here, there])
            return ans
        other = -1
        for i in range(1, 4):
            if i not in (here, there):
                other = i
                break
        hanoi(n-1, here, other, ans)
        hanoi(1, here, there, ans)
        hanoi(n-1, other, there, ans)
        return ans
    ans = hanoi(n, 1, 3, list())
    return ans

n = 2
print(solution(n))