def solution(n, money):
    DIV = 1000000007
    money.sort()
    nm = len(money)
    # cache[i][j] : i까지의 동전으로 j를 만드는 개수
    # cache[i][j] = cache[i-1][j] + cache[i][j-money[i]] 
    # -> i전까지의 동전으로 j를 만드는 개수 + i까지 동전을 써서 j를 만드는 개수
    cache = [[0 for _ in range(n+1)] for _ in range(nm)]
    cache[0][0] = 1
    for j in range(money[0], n+1, money[0]):
        cache[0][j] = 1
    for i in range(1, nm):
        for j in range(n+1):
            if j >= money[i]:
                cache[i][j] = (cache[i-1][j]+cache[i][j-money[i]]) % DIV
            else:
                cache[i][j] = cache[i-1][j]
    return cache[-1][-1]


n = 5
money = [1, 2, 5]
print(solution(n, money))
