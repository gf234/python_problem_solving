#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the swapNodes function below.
#

sys.setrecursionlimit(10000)


def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    class Node:
        def __init__(self):
            self.value = None
            self.leftNode = None
            self.rightNode = None
            self.level = None

        def set_value(self, value):
            self.value = value
            return self

        def set_leftNode(self, leftNode):
            self.leftNode = leftNode
            return self

        def set_rightNode(self, rightNode):
            self.rightNode = rightNode
            return self

        def set_level(self, level):
            self.level = level
            return self

    def in_order_traversal(node, arr):
        if node.leftNode:
            in_order_traversal(node.leftNode, arr)
        arr.append(node.value)
        if node.rightNode:
            in_order_traversal(node.rightNode, arr)
        return arr

    root = Node().set_value(1).set_level(1)
    i = 0

    q = deque()
    q.append(root)
    while q:
        node = q.popleft()

        left, right = indexes[i]
        i += 1

        if left != -1:
            leftNode = Node().set_value(left).set_level(node.level+1)
            node.leftNode = leftNode
            q.append(node.leftNode)

        if right != -1:
            rightNode = Node().set_value(right).set_level(node.level+1)
            node.rightNode = rightNode
            q.append(node.rightNode)

    answers = []

    for k in queries:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()

            if node.level >= k and node.level % k == 0:
                temp = node.leftNode
                node.leftNode = node.rightNode
                node.rightNode = temp

            if node.leftNode:
                q.append(node.leftNode)

            if node.rightNode:
                q.append(node.rightNode)

        answers.append(in_order_traversal(root, []))

    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
