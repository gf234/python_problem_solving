import sys


def input(): return sys.stdin.readline().rstrip()


s = input()
n = len(s)
answer = 0
while True:
    for i in range(0, n-answer):
        sub = s[i:i+answer+1]
        for j in range(i+1, n-answer):
            if sub == s[j:j+answer+1]:
                answer += 1
                break
        else:
            continue
        break
    else:
        break
print(answer)
