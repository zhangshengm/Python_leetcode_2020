# 队列实现栈
# First answer
# 一个队列一边增加一边逆序
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s1.append(x)
        t=len(self.s1)
        while t >1:
            self.s1.append(self.s1.pop(0))
            t=t-1
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.s1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.s1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.s1 else False
      
# 队列实现栈
# Second answer
