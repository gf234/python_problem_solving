import sys
sys.setrecursionlimit(10**9)


def read(): return sys.stdin.readline().rstrip()


preorder = []
while True:
    try:
        preorder.append(int(read()))
    except:
        break


def f(start, end):
    if start > end:
        return
    else:
        root = preorder[start]
        div = end+1
        for i in range(start+1, end+1):
            if root < preorder[i]:
                div = i
                break
        f(start+1, div-1)
        f(div, end)
        print(root)


f(0, len(preorder)-1)
