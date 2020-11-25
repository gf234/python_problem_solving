def possible(infos):
    for x, y, a in infos:
        if a:
            # 보
            if (x, y-1, 0) not in infos and (x+1, y-1, 0) not in infos and ((x+1, y, 1) not in infos or (x-1, y, 1) not in infos):
                return False
        else:
            # 기둥
            if y != 0 and (x, y-1, 0) not in infos and (x, y, 1) not in infos and (x-1, y, 1) not in infos:
                return False
    return True


def solution(n, build_frame):
    infos = set()

    for x, y, a, b in build_frame:
        if b:
            # 설치
            infos.add((x, y, a))
            if not possible(infos):
                infos.remove((x, y, a))
        else:
            # 삭제
            infos.remove((x, y, a))
            if not possible(infos):
                infos.add((x, y, a))
    answer = list(map(list, infos))
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n, build_frame))
