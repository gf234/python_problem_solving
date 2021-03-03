s = input()
n = len(s)
# isPalindrome[i][j]: i~j 까지의 문자가 펠린드롬인지 판별
isPalindrome = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    isPalindrome[i][i] = True
for i in range(n-1):
    isPalindrome[i][i+1] = (s[i] == s[i+1])
for i in range(2, n):
    for j in range(n-i):
        isPalindrome[j][j+i] = isPalindrome[j+1][j+i-1] and (s[j] == s[j+i])
# cache[i]: i까지 고려한 최소 값
cache = [-1 for _ in range(n)]
cache[0] = 1
for end in range(1, n):
    # 전체가 팰린드롬인 경우 1
    if isPalindrome[0][end]:
        cache[end] = 1
    else:
        # 이전까지의 최소 값에 맨뒤에 현재 문자 하나 추가하는 경우
        cache[end] = cache[end-1] + 1
        # 현재 문자를 포함하는 팰린드롬을 만들 수 있지 검색
        for start in range(1, end):
            if isPalindrome[start][end]:
                cache[end] = min(cache[end], cache[start-1] + 1)
print(cache[n-1])
