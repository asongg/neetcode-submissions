class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minimum = float("infinity")
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) != 0:
            app = min(val, self.minstack[len(self.minstack) - 1])
            self.minstack.append(app)
        else:
            self.minstack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack) - 1]