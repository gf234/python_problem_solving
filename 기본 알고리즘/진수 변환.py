# 10진수 -> n진수 변환
def decToN(decimal, n):
    convertedNum = ''
    while decimal != 0:
        remainder = decimal % n

        convertedNum = str(remainder)+convertedNum
        decimal //= n
    return convertedNum


n = 2
num = decToN(256, n)
print(num)

# n진수 -> 10진수 변환


def NToDec(num, n):
    ret = 0
    digit = len(num)-1
    for x in map(int, num):
        ret += x*(n**digit)
        digit -= 1
    return ret


print(NToDec(num, n))


ret = 0
for i in range(3, 1001, 3):
    ret += i
for i in range(5, 1001, 5):
    ret += i
for i in range(15, 1001, 15):
    ret -= i
print(ret)

ret = 0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        ret += i
print(ret)
