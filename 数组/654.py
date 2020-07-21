class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        t,res=[],[]
        s=0
        for i in range(len(nums)):
            if nums[i] not in t:
                t.append(nums[i])
                #去除重复元素的异或值
                s^=nums[i]
            #找到重复元素
            else:
                 res.append(nums[i])
        #找到缺失元素
        for i in range(1,len(nums)+1):
            s^=i
        res.append(s)
        return res


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a,b,s1=0,0,0
        #将nums中所有元素以及[1,len(nums)]的元素异或
        #s1=a^b,a为重复值,b为替换值，肯定不同，找到mask位
        for i in range(len(nums)):
            s1^=(nums[i]^(i+1))
        # mask=1
        # while (s1&mask)==0:
        #       mask<<=1
        mask=s1&(-s1)
        #将上述两组数字分类a与b肯定分到两类
        for k in range(len(nums)):
            if (nums[k]&mask)==0:
               a^=nums[k]
            else:
               b^=nums[k]
            if (k+1)&mask==0:
                a^=(k+1)
            else:
                b^=(k+1)
        for i in range(len(nums)):
            if nums[i]==a:
                return [a,b]
        
        
        return [b,a]
         
        

          
            
