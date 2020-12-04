def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left+right)//2

        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt == k:
                    right = mid-1
                    break
            else:
                cnt = 0
        else:
            left = mid+1

    return left
