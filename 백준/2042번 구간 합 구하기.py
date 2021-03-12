import sys
import math


def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())
nums = [0]
for _ in range(n):
    x = int(input())
    nums.append(x)
# 트리를 구현하기 위해 필요한 배열의 크기는 2**(h+1)-1 이다.
h = math.ceil(math.log2(n))
size = 2**(h+1)
tree = [0 for _ in range(size)]

# 트리 초기화


def initTree(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    tree[node] = initTree(node*2, start, (start+end)//2) + \
        initTree(node*2+1, (start+end)//2+1, end)
    return tree[node]

# 구간합 구하기


def subSum(node, start, end, left, right):
    # 범위를 벗어나면 0을 리턴한다.
    if left > end or right < start:
        return 0
    # 구해야할 범위 안쪽에 있으면 바로 합을 리턴한다.
    if left <= start and end <= right:
        return tree[node]
    # 왼쪽과 오른쪽 서브트리를 탐색한다.
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2+1, (start+end)//2+1, end, left, right)

# 값 변경


def update(node, start, end, index, diff):
    # 범위에 해당 값이 포함이 안되면 바로 리턴한다.
    if index < start or index > end:
        return
    # 루트부터 구간합을 변경해준다.
    tree[node] += diff
    # 리프노드까지 실행
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2 + 1, end, index, diff)


initTree(1, 1, n)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - nums[b]
        nums[b] = c
        update(1, 1, n, b, diff)
    else:
        print(subSum(1, 1, n, b, c))
