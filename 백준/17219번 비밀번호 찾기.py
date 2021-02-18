import sys

n, m = map(int, input().split())
passwords = dict()
for _ in range(n):
    site, password = sys.stdin.readline().rstrip().split()
    passwords[site] = password

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(passwords[site])
