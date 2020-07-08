class Solution:
    def minArray(self, numbers: List[int]) -> int:
        res=float('inf')
        for i in range(len(numbers)):
            if numbers[i]<res:
                res=numbers[i]
        return res
        
class Solution:
    def minArray(self, numbers: List[int]) -> int:
       i,j=0,len(numbers)-1
       while i <=j:
             m=(i+j)//2
             #如果中间值大于最右端的值，m在左排序数组，最小值点在右排序数组，[m+1,j]
             if numbers[m]>numbers[j]: 
                 i=m+1
             #如果中间值小于最右端的值，m在右排序数组，最小值点在右排序数组，[i,m]
             elif numbers[m]<numbers[j]:
                 j=m
             #如果相等，缩小范围
             else:
                 j=j-1
       return numbers[i]
