# First answer
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]
        self.minvalue=[]
    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> None:
        t=self.s1[-1]
        del self.s1[-1]
        return t

    def top(self) -> int:
        return self.s1[-1]

    def min(self) -> int:
        val=self.s1[0]
        for i in self.s1:
            if i < val:
                val=i
        return val
