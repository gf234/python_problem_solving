def check(bid, uid):
    if len(bid) != len(uid):
        return False
    for i, c in enumerate(bid):
        if c == '*':
            continue
        if c != uid[i]:
            return False
    return True


def find_banned_it(ans, n, ind, possible_id, choosed):
    if ind == n:
        ans.add(frozenset(choosed))
        return

    for pid in possible_id[ind]:
        if pid not in choosed:
            choosed.add(pid)
            find_banned_it(ans, n, ind+1, possible_id, choosed)
            choosed.remove(pid)
    return


def solution(user_id, banned_id):
    ans = set()

    possible_id = [set() for _ in range(len(banned_id))]
    # banned_id 마다 user_id 매칭되는 아이디가 있는지 확인
    for i, bid in enumerate(banned_id):
        for uid in user_id:
            if check(bid, uid):
                possible_id[i].add(uid)
    find_banned_it(ans, len(possible_id), 0, possible_id, set())

    return len(ans)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
