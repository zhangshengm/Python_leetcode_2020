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
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1=[]

    def addNum(self, num: int) -> None:
        if not self.s1: self.s1.append(num)
        else:
            #flag代表是否插入元素
            flag=0
            i,j=0,len(self.s1)-1
            while i<=j:
                  mid=(i+j)//2
                  if num <self.s1[mid]:j=mid-1
                  elif num > self.s1[mid]: i=mid+1
                  else: 
                      #如果找到该元素，则插入
                      flag=1
                      self.s1.insert(mid,num)
                      break
            #没有找到该元素，则按排序的位置i插入元素
            if flag==0:         
               self.s1.insert(i,num)

    def findMedian(self) -> float:
        t=len(self.s1)
        if t==0:
           return 
        if t%2==0:
            return (self.s1[t//2]+self.s1[t//2-1])/2
        else:
            return self.s1[t//2]
        
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #A[0]是A中最小值
        #B[0]是B中最大值
        self.A=[]
        self.B=[]

    def addNum(self, num: int) -> None:
        if len(self.A)==len(self.B):
            heappush(self.B,-num)
            #-heappop(self.B)即为B中最大值
            heappush(self.A,-heappop(self.B))
        else:
            heappush(self.A,num)
            #heappop(self.A)为A中最小值
            heappush(self.B,-heappop(self.A))

    def findMedian(self) -> float:
        return self.A[0] if (len(self.A)+len(self.B))%2==1 else (self.A[0]-self.B[0])/2


