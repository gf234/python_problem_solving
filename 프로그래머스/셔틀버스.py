from datetime import datetime, timedelta


def solution(n, t, m, timetable):
    ans = ""
    arrive = datetime.strptime("09:00", "%H:%M")
    timetable.sort()

    i = 0
    for _ in range(n):
        cnt = 0
        possible = True
        for j in range(i, len(timetable)):
            if arrive.strftime("%H:%M") >= timetable[j]:
                cnt += 1
                if cnt == m:
                    ans = (datetime.strptime(timetable[j], "%H:%M") -
                           timedelta(minutes=1)).strftime("%H:%M")
                    possible = False
                    i = j+1
                    break
            else:
                i = j
                break
        if possible:
            ans = arrive.strftime("%H:%M")
        arrive += timedelta(minutes=t)
    return ans


n = 2
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))
