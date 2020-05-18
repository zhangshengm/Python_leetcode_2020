# First answer
#Execution time nearly：1308 ms
#Consumed memory nearly: 16.8 MB
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

        del self.s1[-1]
    
    def top(self) -> int:
        return self.s1[-1]

    def min(self) -> int:
        val=self.s1[0]
        for i in self.s1:
            if i < val:
                val=i
        return val

# Second answer
#Execution time nearly：84 ms
#Consumed memory nearly: 17 MB
#思路如下: 1.考虑用额外栈存储最小值，把最小值元素放到栈顶（当最小值有重复值如何考虑？）
#         2.原始栈在元素出栈时，会影响到额外栈（该元素是否为最小值）
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]
        self.minvalue=[]
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.minvalue or x <= self.minvalue[-1]:
           self.minvalue.append(x)
        
    def pop(self) -> None:
        if self.s1.pop() == self.minvalue[-1]:
            self.minvalue.pop()

    def top(self) -> int:
        return self.s1[-1]

    def min(self) -> int:
        return self.minvalue[-1]
