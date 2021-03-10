import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
ips = []
for _ in range(n):
    ip = list(map(int, input().split('.')))
    ips.append(ip)

network = []
mask = []
m = 0
for i in range(4):
    for j in range(n-1):
        if ips[j][i] != ips[j+1][i]:
            break
    else:
        network.append(ips[0][i])
        mask.append(255)
        continue
    pos = 7
    while True:
        x = 1 << pos
        for j in range(n-1):
            if ips[j][i] & x != ips[j+1][i] & x:
                m = (3-i)*8+pos+1
                temp = 0
                # pos = 0~7
                # 7-pos 만큼 1
                for _ in range(7-pos):
                    temp = (temp << 1) + 1
                temp = temp << (pos+1)
                network.append(temp & ips[j][i])
                mask.append(temp)
                for _ in range(i+1, 4):
                    network.append(0)
                    mask.append(0)
                break
        else:
            pos -= 1
            continue
        break
    break

print('.'.join(map(str, network)))
print('.'.join(map(str, mask)))
