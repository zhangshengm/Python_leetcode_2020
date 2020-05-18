#First answer:
#Execution time nearly：40 ms
#Consumed memory nearly: 13.7 MB
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.s1 else True
