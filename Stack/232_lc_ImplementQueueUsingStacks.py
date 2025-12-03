class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Queue empty cannot pop")
        self.transfer_stack1_stack2()
        return self.stack2.pop()

    def peek(self) -> int:
        if self.empty():
            raise IndexError("Queue empty cannot peek")
        self.transfer_stack1_stack2()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def transfer_stack1_stack2(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


obj = MyQueue()
obj.push(10)
obj.push(200)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_4)