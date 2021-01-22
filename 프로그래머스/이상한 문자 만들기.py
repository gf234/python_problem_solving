import re


def solution(s):
    answer = ""
    # 단어들을 찾는다.
    words = s.split()
    # 공백들을 찾는다.
    spaces = re.compile('( +)').findall(s)
    si = 0
    # 처음에 공백으로 시작하는 경우 공백을 먼저 넣어준다.
    if s[0] == ' ':
        answer += spaces[si]
        si += 1
    # 단어를 변환해서 넣어준다.
    for word in words:
        for j, c in enumerate(word):
            if j % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        if si < len(spaces):
            answer += spaces[si]
            si += 1
    return answer
