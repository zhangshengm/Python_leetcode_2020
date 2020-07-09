class Solution:
    # 时间复杂度: O(n)
    #空间复杂度: O(n)
    def exchange(self, nums: List[int]) -> List[int]:
        t1,t2=[],[]
        for i in nums:
            if i%2!=0:
                t1.append(i)
            else:
                t2.append(i)
        return t1+t2

class Solution:
    # 时间复杂度: O(n)
    #空间复杂度: O(1)
    def exchange(self, nums: List[int]) -> List[int]:
        #首尾双指针
        i,j=0,len(nums)-1
        while i<j:
            #如果前为
            if nums[i]%2==0 and nums[j]%2!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            if nums[i]%2!=0:
                i+=1
            if nums[j]%2==0:
                j-=1
     
        return nums
            
