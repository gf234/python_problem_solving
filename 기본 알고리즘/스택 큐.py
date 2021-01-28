class StackQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, data):
        self.inStack.append(data)

    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()


stackQueue = StackQueue()
stackQueue.push(1)
stackQueue.push(2)
print(stackQueue.pop())
stackQueue.push(3)
stackQueue.push(4)
print(stackQueue.pop())
stackQueue.push(5)
print(stackQueue.pop())
print(stackQueue.pop())
print(stackQueue.pop())
