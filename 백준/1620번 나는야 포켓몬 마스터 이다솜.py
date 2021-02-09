import sys

n, m = map(int, input().split())

pokemonDict = dict()
numDict = dict()
for i in range(1, n+1):
    pokemon = sys.stdin.readline().rstrip()
    pokemonDict[i] = pokemon
    numDict[pokemon] = i

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if '0' <= q[0] <= '9':
        print(pokemonDict[int(q)])
    else:
        print(numDict[q])
