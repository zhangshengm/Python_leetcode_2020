#栈实现队列
#（1）判定栈为空的条件
#（2）考虑返回栈顶元素 peek()、出栈函数pop()以及push()函数先后顺序，都要将元素转移到第二个数组
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
#         if self.empty():
#             return
        if not self.s2:
           while self.s1:
               self.s2.append(self.s1.pop())
           return self.s2.pop()
        else:
           return self.s2.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
#         if self.empty():
#             return
        if not self.s2:
           while self.s1:
               self.s2.append(self.s1.pop())
           return self.s2[-1]
        else:
           return self.s2[-1]
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if (not self.s2) and (not self.s1) else False
