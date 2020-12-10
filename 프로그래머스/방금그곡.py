from datetime import datetime, timedelta
import re


def solution(m, musicinfos):
    ans = ["(None)", 0]
    for s in musicinfos:
        info = s.split(',')
        start, end, title, melody = info
        playTime = (datetime.strptime(end, "%H:%M") -
                    datetime.strptime(start, "%H:%M")).seconds // 60
        ind = 0
        playMelody = ""
        for _ in range(playTime):
            mchar = melody[ind]
            nextChar = 'X'
            if ind+1 < len(melody):
                nextChar = melody[ind+1]

            if nextChar != '#':
                playMelody += mchar
                ind += 1
            else:
                playMelody += mchar + '#'
                ind += 2
            if ind == len(melody):
                ind = 0

        parser = re.compile(f"{m}(?!#)")
        mfind = re.findall(parser, playMelody)
        if mfind and ans[1] < playTime:
            ans[0] = title
            ans[1] = playTime
    return ans[0]


m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
print(solution(m, musicinfos))
