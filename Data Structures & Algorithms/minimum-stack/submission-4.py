class MinStack:

    def __init__(self):
        self.stack : List[int] = []
        self.minStack : List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
