def solution(left, right):
    answer = 0
    
    def findDivisor(num):
        if num == 1:
            return -1
        cnt = 2
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        
        if cnt % 2 == 0:
            return num
        else:
            return -num
    
    for i in range(left, right+1):
        answer += findDivisor(i)
    
    return answer