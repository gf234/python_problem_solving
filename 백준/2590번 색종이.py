import sys
import math


def input(): return sys.stdin.readline().rstrip()


papers = [0]
for _ in range(6):
    papers.append(int(input()))

# 6
answer = papers[6]
# 5
answer += papers[5]
papers[1] -= 11*papers[5]
# 4
answer += papers[4]
papers[2] -= 5*papers[4]
if papers[2] < 0:
    papers[1] -= -papers[2]*4
    papers[2] = 0
# 3
answer += math.ceil(papers[3]/4)
remain = 4 - papers[3] % 4
if remain == 1:
    if papers[2] > 0:
        papers[2] -= 1
        papers[1] -= 5
    else:
        papers[1] -= 9
elif remain == 2:
    if papers[2] == 0:
        papers[1] -= 18
    else:
        papers[2] -= 3
        papers[1] -= 6
        if papers[2] < 0:
            papers[1] -= -papers[2]*4
            papers[2] = 0
elif remain == 3:
    if papers[2] == 0:
        papers[1] -= 27
    else:
        papers[2] -= 5
        papers[1] -= 7
        if papers[2] < 0:
            papers[1] -= -papers[2]*4
            papers[2] = 0
# 2
answer += math.ceil(papers[2] / 9)
remain = 9 - papers[2] % 9
if remain != 9:
    papers[1] -= remain*4
# 1
if papers[1] < 0:
    papers[1] = 0
answer += math.ceil(papers[1] / 36)
print(answer)
