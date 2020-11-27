import bisect
n = int(input())
A = list(map(int, input().split()))

stack = [0]

for i, a in enumerate(A):
    # 마지막 원소보다 크면 삽입
    if stack[-1] < a:
        stack.append(a)
    # 마지막 원소보다 작으면, 이분 탐색으로 a가 들어갈 위치를 찾은 후 바꾼다.
    # 주의! 실제로 stack에 증가하는 부분 수열이 담기는 것은 아니다. 중간에 정의와 맞지 않는 값이 들어갈 수 있다.
    # ex) 1 3 5 2 9
    # stack) 1 2 5 9
    # real)  1 3 5 9
    else:
        stack[bisect.bisect_left(stack, a)] = a


print(len(stack)-1)
