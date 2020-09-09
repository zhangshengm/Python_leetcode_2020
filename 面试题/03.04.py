class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A=[]
        self.B=[]


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)

    #弹出队首元素
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #先看弹出元素的栈
        if self.B: 
            return self.B.pop()
        else:
            #再看压入栈是否有元素
            if not self.A: return False
            while self.A:
                tmp=self.A.pop()
                self.B.append(tmp)
            return self.B.pop()
        
    #输出队首元素
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.B: 
            return self.B[-1]
        else:
            #再看压入栈是否有元素
            if not self.A: return False
            while self.A:
                tmp=self.A.pop()
                self.B.append(tmp)
            return self.B[-1]
            
    #如果出队，入队队列都为空，则队为空
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.A and not self.B:
           return True
        else:
            return False





# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
