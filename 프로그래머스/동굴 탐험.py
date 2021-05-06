def solution(n, path, order):
    adj = [[] for _ in range(n)]
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    before_to_after = dict()
    disable = set()
    for before, after in order:
        before_to_after[before] = after
        disable.add(after)
    
    if 0 in disable:
        return False
    
    def dfs():
        stack = [0]
        visited = [False for _ in range(n)]
        visited[0] = True
        temp = set()
        while stack:
            here = stack.pop()

            if here in before_to_after:
                after = before_to_after[here]
                disable.remove(after)
                if after in temp:
                    visited[after] = True
                    stack.append(after)
                    temp.remove(after)

            for there in adj[here]:
                if visited[there]:
                    continue
                if there in disable:
                    temp.add(there)
                else:
                    visited[there] = True
                    stack.append(there)
        if temp:
            return False
        return True

    return dfs()
