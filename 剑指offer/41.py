class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]

    def addNum(self, num: int) -> None:
        self.s1.append(num)
        self.s1.sort()

    def findMedian(self) -> float:
        t=len(self.s1)
        if t==0:
           return 
        if t%2==0:
            return (self.s1[t//2]+self.s1[t//2-1])/2
        else:
            return self.s1[t//2]
