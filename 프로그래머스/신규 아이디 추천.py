import re


def solution(new_id: str):
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub(r'[^0-9a-z-_.]', '', new_id)
    # 3
    new_id = re.sub(r'[.]+', '.', new_id)
    # 4
    new_id = re.sub(r'^[.]|[.]$', '', new_id)
    # 5
    if not new_id:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7
    l = len(new_id)
    if l <= 2:
        new_id += new_id[-1]*(3-l)
    return new_id
