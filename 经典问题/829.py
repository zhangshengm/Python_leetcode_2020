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
