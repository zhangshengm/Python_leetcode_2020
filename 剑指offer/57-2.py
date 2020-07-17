class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        t,res=target//2+1,[]
        i,j,tmp=1,2,1
        while i<t and j<=t:
              #如果当前累加值小于target,j往后移动
              if tmp+j<target:
                 tmp+=j
                 j+=1
              else:
                  #如果累加值等于target,将结果放入res列表中
                  if tmp+j==target:
                     res.append(list(range(i,j+1)))
                  #如果累加值大于等于target,更新i,j,tmp
                  i+=1
                  tmp=i
                  j=i+1
        return res
        

                 
                 
        

