import sys


def input(): return sys.stdin.readline().rstrip()


a, b = map(int, input().split())
mat = [[0 for _ in range(a+1)] for _ in range(b+1)]
n, m = map(int, input().split())
robots = [0]
for i in range(1, n+1):
    x, y, direction = input().split()
    x = int(x)
    y = int(y)
    robots.append((x, y, direction))
    mat[y][x] = i
operations = []
for _ in range(m):
    robot, operation, count = input().split()
    robot = int(robot)
    count = int(count)
    operations.append((robot, operation, count))


def solve():
    dxy = {'E': (0, 1), 'W': (0, -1), 'S': (-1, 0), 'N': (1, 0)}
    left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    for robot, operation, count in operations:
        x, y, direction = robots[robot]

        if operation == 'F':
            mat[y][x] = 0
            for _ in range(count):
                y = y + dxy[direction][0]
                x = x + dxy[direction][1]
                if x <= 0 or y <= 0 or x > a or y > b:
                    print(f'Robot {robot} crashes into the wall')
                    return
                elif mat[y][x] != 0:
                    print(f'Robot {robot} crashes into robot {mat[y][x]}')
                    return
            mat[y][x] = robot
        elif operation == 'L':
            for _ in range(count):
                direction = left[direction]
        else:
            for _ in range(count):
                direction = right[direction]
        robots[robot] = (x, y, direction)
    print('OK')
    return


solve()
