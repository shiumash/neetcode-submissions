class MinStack:

    def __init__(self):
        self.v = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.v.append(val)
        mv = min(self.minstack[-1] if self.minstack else val, val)
        self.minstack.append(mv)

    def pop(self) -> None:
        self.v.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.v[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
