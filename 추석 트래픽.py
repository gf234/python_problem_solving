import datetime


def calcThroughput(b, infos):
    a = b - datetime.timedelta(seconds=0.999)
    c = b + datetime.timedelta(seconds=0.999)
    back = 0
    forth = 0
    for start, end in infos:
        if not (end < b or start > c):
            forth += 1
        if not (end < a or start > b):
            back += 1

    return max(back, forth)


def solution(lines):
    answer = 0

    infos = []
    for line in lines:
        date, time, s = line.split()
        s = float(s[:-1])-0.001
        end = datetime.datetime.strptime(
            date+' '+time, '%Y-%m-%d %H:%M:%S.%f')
        start = end - datetime.timedelta(seconds=s)
        infos.append((start, end))

    for start, end in infos:
        answer = max(answer, calcThroughput(
            start, infos), calcThroughput(end, infos))

    return answer


lines = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']


print(solution(lines))
