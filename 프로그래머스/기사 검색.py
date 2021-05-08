import bisect
from collections import defaultdict


def count_by_range(temp, start, end):
    return bisect.bisect_right(temp, end) - bisect.bisect_left(temp, start)


def solution(words, queries):
    answer = []
    len_to_words = defaultdict(list)
    len_to_reversed_words = defaultdict(list)
    for word in words:
        l = len(word)
        len_to_words[l].append(word)
        len_to_reversed_words[l].append(word[::-1])
    for words in len_to_words.values():
        words.sort()
    for words in len_to_reversed_words.values():
        words.sort()
    for query in queries:
        l = len(query)
        if query[0] == '?':
            temp = len_to_reversed_words[l]
            start = query[::-1].replace('?', 'a')
            end = query[::-1].replace('?', 'z')
        else:
            temp = len_to_words[l]
            start = query.replace('?', 'a')
            end = query.replace('?', 'z')
        answer.append(count_by_range(temp, start, end))
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
