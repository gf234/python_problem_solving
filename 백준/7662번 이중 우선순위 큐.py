import heapq
import sys


t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    minHeap = []
    maxHeap = []
    removed = set()
    size = 0
    for i in range(k):
        c, n = sys.stdin.readline().rstrip().split()
        n = int(n)

        if c == 'I':
            size += 1
            # i 를 같이 저장해서 각 값의 id 로 사용하여 삭제여부를 확인한다.
            heapq.heappush(minHeap, (n, i))
            heapq.heappush(maxHeap, (-n, i))
        elif n == 1:
            if size == 0:
                continue
            while maxHeap:
                temp = heapq.heappop(maxHeap)
                if temp[1] in removed:
                    continue
                removed.add(temp[1])
                break
            size -= 1
        else:
            if size == 0:
                continue
            while minHeap:
                temp = heapq.heappop(minHeap)
                if temp[1] in removed:
                    continue
                removed.add(temp[1])
                break
            size -= 1

    if size == 0:
        print("EMPTY")
    else:
        # 힙의 상태가 다를 수 있으므로 마지막으로 처리해준다.
        while maxHeap:
            temp = heapq.heappop(maxHeap)
            if temp[1] in removed:
                continue
            print(-temp[0], end=' ')
            break
        while minHeap:
            temp = heapq.heappop(minHeap)
            if temp[1] in removed:
                continue
            print(temp[0])
            break
