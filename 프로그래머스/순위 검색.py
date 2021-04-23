from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    scores = defaultdict(list)
    for s in info:
        s = s.split()
        score = int(s.pop())
        for n in range(1, 5):
            for key in combinations(s, n):
                scores[key].append(score)
        scores[()].append(score)
        
    for x in scores:
        scores[x].sort()
    
    result = []
    for q in query:
        q = q.split()
        minScore = int(q.pop())
        key = []
        for x in q:
            if x != '-' and x != 'and':
                key.append(x)
        temp = scores[tuple(key)]
        i = bisect.bisect_left(temp, minScore)
        cnt = len(temp)-i
        result.append(cnt)
    return result