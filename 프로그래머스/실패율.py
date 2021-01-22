def solution(N, stages):
    reachNums = [0 for _ in range(N+1)]
    stuckNums = [0 for _ in range(N+1)]

    for stage in stages:
        for i in range(1, stage+1):
            if i <= N:
                reachNums[i] += 1
        if stage <= N:
            stuckNums[stage] += 1

    failuerRates = []
    for i in range(1, N+1):
        if reachNums[i] != 0:
            failuerRates.append((-(stuckNums[i]/reachNums[i]), i))
        else:
            failuerRates.append((0, i))
    failuerRates.sort()

    return [x[1] for x in failuerRates]
