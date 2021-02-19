n = int(input())
adj = []
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)


def floyd_warshall():
    for v in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][j] == 1:
                    continue
                if adj[i][v] + adj[v][j] == 2:
                    adj[i][j] = 1


floyd_warshall()
for row in adj:
    print(' '.join(map(str, row)))
