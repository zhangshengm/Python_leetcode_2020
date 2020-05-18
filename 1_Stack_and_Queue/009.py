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
            if len(self.s2)>=1:
                self.s2.pop(0)
            self.s2.append(self.s1.pop(0))

            return self.s2[0]
#Second answer:
#Execution time nearly： ms
#Consumed memory nearly:  MB
#
