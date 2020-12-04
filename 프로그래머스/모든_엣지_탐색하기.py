from collections import defaultdict, deque
import math


def solution(tickets):
    answer = []

    adj = defaultdict(list)

    for a, b in tickets:
        adj[a].append(b)

    for a, _ in tickets:
        adj[a].sort()

    l = len(tickets)

    def dfs(possible, cnt, here):
        if cnt == l+1:
            return [here]

        ret = [here]
        for i, there in enumerate(possible[here]):
            possible[here].remove(there)
            d = dfs(possible, cnt+1, there)
            ret += d
            if len(d) >= 1:
                return ret
            possible[here].insert(i, there)
        else:
            return []
    answer = dfs(adj, 1, 'ICN')
    return answer


tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], [
    'SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]

t2 = [['ICN','A'],['ICN','B'],['B','ICN']]
print(solution(t2))
