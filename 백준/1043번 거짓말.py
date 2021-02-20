n, m = map(int, input().split())

knows = set(list(map(int, input().split()))[1:])

adj = [[] for _ in range(n+1)]
parties = []
for _ in range(m):
    attendees = list(map(int, input().split()))[1:]
    for i in range(len(attendees)-1):
        a, b = attendees[i], attendees[i+1]
        adj[a].append(b)
        adj[b].append(a)
    parties.append(attendees)

visited = set()
temp = []
for i in knows:
    def bfs(start, visited, temp):
        stack = []
        stack.append(start)
        visited.add(start)
        while stack:
            here = stack.pop()

            for there in adj[here]:
                if there not in visited:
                    visited.add(there)
                    temp.append(there)
                    stack.append(there)

    if i not in visited:
        bfs(i, visited, temp)
knows.update(temp)

answer = 0
for attendees in parties:
    for x in attendees:
        if x in knows:
            break
    else:
        answer += 1
print(answer)
