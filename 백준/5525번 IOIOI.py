n = int(input())
p = 'IO'*n+'I'
m = int(input())
s = input()

count = 0
i = 0
while i < m:
    if s[i] == 'I' and s[i:i+n*2+1] == p:
        count += 1
        j = i+n*2+1
        while j+1 < m:
            if s[j] != 'O' or s[j+1] != 'I':
                break
            count += 1
            j += 2
        i = j-1
    else:
        i += 1
print(count)
