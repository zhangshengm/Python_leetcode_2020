class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(32):
            bit=1<<i
            count=0
            for n in nums:
                #n&bit，因为bit只有1位为1，所以判断n对应的这一位是否为0
                if n&bit!=0:
                   count+=1
            #3为其他元素出现的次数
            if count%3!=0:
                #或运算,把当前的1加到对应位置上
                res|=bit
        return res if res<=2**31-1 else res-2**32
