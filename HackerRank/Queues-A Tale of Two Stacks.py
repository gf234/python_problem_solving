from collections import deque


class MyQueue(object):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def pop(self):
        self.head = self.head.next
        if self.head == None:
            self.tail = None

    def put(self, value):
        node = self.Node(value)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
