def solution(n, words):
    end = words[0][0]
    wrong = set()
    for i, word in enumerate(words):
        start = word[0]
        if start != end or len(word) == 1 or word in wrong:
            user = i % n + 1
            num = i//n + 1
            return [user, num]
        else:
            wrong.add(word)
            end = word[-1]
    return [0, 0]


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
