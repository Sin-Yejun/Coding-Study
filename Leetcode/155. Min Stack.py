class MinStack:

    def __init__(self):
        self.li = []

    def push(self, val: int) -> None:
        self.li.append(val)
        return None

    def pop(self) -> None:
        self.li = self.li[:len(self.li)-1]
        return None

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return min(self.li)
