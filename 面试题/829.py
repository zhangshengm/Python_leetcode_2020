from collections import deque
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N<=2:
           return 1
        tmp,i,flag=0,(N//2+1),1
        nums=deque()
        while i>=1:
              nums.append(i)
              t=tmp+i
              if t<N:
                 tmp=t
              elif t==N:
                   flag+=1
                   tmp=t-nums.popleft()
              else:
                   if nums:
                      tmp=t-nums.popleft()
              i-=1
        return flag

from collections import deque
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        tmp=0
        # (x+1)(x+2)(x+k)=N, (x+1+x+k)(k)/2=N
        #2N=k(2x+k+1), k<2N**(1/2)
        y=int((2*N)**(1/2))+1
        for k in range(1,y):
            if 2*N%k==0:
               x=(2*N/k-k-1)
               if x%2==0 and x>=0:
                  tmp+=1
        return tmp
