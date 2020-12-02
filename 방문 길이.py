def possible(i, j):
    if -5 <= i <= 5 and -5 <= j <= 5:
        return True
    return False


def solution(dirs):
    proad = set()

    here = (0, 0)
    dxy = dict()
    dxy['U'] = (1, 0)
    dxy['D'] = (-1, 0)
    dxy['R'] = (0, 1)
    dxy['L'] = (0, -1)

    for dir in dirs:
        dx, dy = dxy[dir]
        x, y = here[0]+dx, here[1]+dy
        if possible(x, y):
            proad.add(frozenset((here, (x, y))))
            here = (x, y)
    
    return len(proad)

dirs = 'ULURRDLLU'
print(solution(dirs))