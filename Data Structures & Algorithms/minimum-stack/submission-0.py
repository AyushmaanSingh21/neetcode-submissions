class MinStack:

    def __init__(self):
        stack = []
        MinStack = []
        

    def push(self, val: int) -> None:
        stack.append(val)
        val = min(val, MinStack[-1] if MinStack else val)
        MinStack.append(val)
        

    def pop(self) -> None:
        stack.pop()
        MinStack.pop()
        

    def top(self) -> int:
        return stack[-1]
        

    def getMin(self) -> int:
        return MinStack[-1]
        
