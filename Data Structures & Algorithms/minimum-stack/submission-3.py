class MinStack:

    def __init__(self):
        self.stack = []
        self.counter = 0
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(int(val))
        if self.counter == 0:
            self.min_stack.append(val)
            
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

        self.counter += 1

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.counter -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
