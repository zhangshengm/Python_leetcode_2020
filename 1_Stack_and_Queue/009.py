#First answer:
#Execution time nearly：624 ms
#Consumed memory nearly: 17 MB
class CQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def appendTail(self, value: int) -> None:
        self.s1.append(value)
        
    def deleteHead(self) -> int:
        if len(self.s1)==0:
            return -1
        else:
            self.s2.append(self.s1.pop(0))
            return self.s2.pop()
#Second answer:
#Execution time nearly： 550 ms
#Consumed memory nearly:  16.8 MB
class CQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def appendTail(self, value: int) -> None:
        self.s1.append(value)
        
    def deleteHead(self) -> int:
        if self.s2:
            return self.s2.pop()
        if len(self.s1)==0:
            return -1
        else:
            while self.s1:
               self.s2.append(self.s1.pop())
            return self.s2.pop()
