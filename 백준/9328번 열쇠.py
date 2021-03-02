import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    mat = []
    for _ in range(h):
        row = list(input())
        mat.append(row)
    # 가지고 있는 키
    keys = set(list(input()))
    # 키가 없어 못여는 방
    temp = defaultdict(list)

    visited = set()

    def dfs(start):
        stack = []
        stack.append(start)
        visited.add(start)
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        count = 0
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                    c = mat[nx][ny]
                    if c == '*':
                        continue
                    if c == '.':
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                    elif c == '$':
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        count += 1
                    # 대문자인 경우
                    elif c.isupper():
                        if c.lower() in keys:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
                        else:
                            temp[c.lower()].append((nx, ny))
                    # 소문자인 경우
                    else:
                        keys.add(c)
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        if c in temp:
                            for pos in temp[c]:
                                visited.add(pos)
                                stack.append(pos)
        return count

    # 들어갈 수 있는 출입구 찾기

    def calc(i, j):
        ret = 0
        c = mat[i][j]
        if (i, j) in visited or c == '*':
            return 0
        if c == '.':
            ret += dfs((i, j))
        elif c == '$':
            ret += dfs((i, j)) + 1
        elif c.isupper():
            if c.lower() in keys:
                ret += dfs((i, j))
            else:
                temp[c.lower()].append((i, j))
        else:
            keys.add(c)
            ret += dfs((i, j))
            if c in temp:
                for pos in temp[c]:
                    ret += dfs(pos)
        return ret

    answer = 0
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                answer += calc(i, j)
        else:
            answer += calc(i, 0)
            answer += calc(i, w-1)
    print(answer)
