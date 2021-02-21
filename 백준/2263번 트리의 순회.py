import sys

sys.setrecursionlimit(100001)
n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder 값의 인덱스를 저장
pos = [0 for _ in range(n+1)]
for i in range(n):
    pos[inorder[i]] = i


def preorder(in_start, in_end, p_start, p_end):
    if in_start > in_end or p_start > p_end:
        return
    # postorder 의 맨끝은 root 가 된다.
    root = postorder[p_end]
    print(root, end=' ')
    # root 를 기준으로 왼쪽과 오른쪽의 개수를 구한다.
    left = pos[root] - in_start
    right = in_end - pos[root]

    preorder(in_start, pos[root]-1, p_start, p_start + left-1)
    preorder(pos[root]+1, in_end, p_end-right, p_end-1)


preorder(0, n-1, 0, n-1)
print()
