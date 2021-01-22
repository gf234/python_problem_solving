def solution(s, n):
    answer = ""
    for c in s:
        if c == ' ':
            answer += c
        elif ord(c) <= ord('Z'):
            num = ord(c) + n
            if num > ord('Z'):
                num -= 26
            answer += chr(num)
        else:
            num = ord(c) + n
            if num > ord('z'):
                num -= 26
            answer += chr(num)
    return answer
