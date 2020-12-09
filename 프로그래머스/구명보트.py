from collections import deque

def solution(people, limit):
    answer = 0

    people = deque(sorted(people))

    while people:
        heavy = people.pop()
        
        remain = limit-heavy
        while people:
            light = people.popleft()
            if remain >= light:
                remain -= light
            else:
                people.appendleft(light)
                break
        answer += 1
        
    return answer
