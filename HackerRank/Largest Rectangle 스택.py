#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.


def largestRectangle(h):
    # 하나 넣고 시작
    stack = [0]

    answer = -1
    for i in range(1, len(h)):
        # stack top 보다 현재 높이가 더 크거나 같으면 넣어준다.
        if h[i] >= h[stack[-1]]:
            stack.append(i)
        else:
            # stack top이 더 크면 pop하고 사각형의 크기를 계산한다.
            while h[stack[-1]] > h[i]:
                j = stack.pop()
                height = h[j]
                if stack:
                    # stack에 값이 아직 남아있으면 다음과 같이 계산한다.
                    # 앞으로 이동하면서 크거나 같을때만 스택에 넣었기 때문에 width를 i-stack[-1]-1로 계산할 수 있다.
                    # i-stack[-1]-1로 계산하는 이유는 stack top의 한칸 앞까지는 height보다 크거나 같을 수 밖에 없기 때문이다.
                    # stack top에 height보다 작은 값이 있다고 가정하면 stack top 그 작은 값을 만났을 때 이미 빠졌어야 하기 때문에 모순이다.
                    # 즉, stack top의 한칸 앞까지는 height보다 크거나 같다
                    answer = max(answer, height*(i-stack[-1]-1))
                else:
                    # stack이 비었을 때 i를 곱해주는 이유는 스택이 비었다는 것은 해당 값이 i 전까지의 최소 값이 되기 때문이다.
                    answer = max(answer, height*i)
                    break
            stack.append(i)
    else:
        # 마지막에 스택이 아직 비어있지 않다면 계산해준다.
        i = len(h)
        while stack:
            height = h[stack.pop()]
            if stack:
                answer = max(answer, height*(i-stack[-1]-1))
            else:
                answer = max(answer, height*i)
    return answer


if __name__ == '__main__':

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
