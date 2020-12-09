def solution(record):
    user_id = dict()

    temp = []
    for s in record:
        a = s.split()
        if a[0] == 'Enter':
            temp.append((a[0], a[1]))
            user_id[a[1]] = a[2]
        if a[0] == 'Leave':
            temp.append((a[0], a[1]))
        if a[0] == 'Change':
            user_id[a[1]] = a[2]

    ans = []
    for op, uid in temp:
        if op == 'Enter':
            ans.append(user_id[uid]+"님이 들어왔습니다.")
        if op == 'Leave':
            ans.append(user_id[uid]+"님이 나갔습니다.")
    return ans
