from itertools import permutations


def solution(n, data):
    name = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    ind = [i for i in range(8)]
    nameToInd = {name: ind for name, ind in zip(name, ind)}
    answer = 0
    for permut in permutations(ind):
        for str in data:
            left, _, right, op, num = str
            num = int(num)
            interval = abs(permut[nameToInd[left]] -
                           permut[nameToInd[right]])-1
            if op == '=' and interval != num:
                break
            if op == '>' and interval <= num:
                break
            if op == '<' and interval >= num:
                break
        else:
            answer += 1
    return answer


n = 2
data = ["N~F=0", "R~T>2"]
print(solution(n, data))
