class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize=maxSize
        self.s1=[]

    def push(self, x: int) -> None:
        if len(self.s1)<self.maxsize:
           self.s1.append(x)

    def pop(self) -> int:
        if self.s1:
           return self.s1.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
     
        # if not self.s1:
        #  return
        if k>=len(self.s1):
           self.s1=[i+val for i in self.s1]
        else:   
           for i in range(0,k):
               self.s1[i]=self.s1[i]+val
           
        
