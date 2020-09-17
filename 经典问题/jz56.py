class Solution:
    #注意div为1,10,100,1000,找到的是与运算的和中中从右往左第一个为1的位置
    #该位置的div与各个数字做与运算，可以通过判断是否为0，将数字分成两组
    def singleNumbers(self, nums: List[int]) -> List[int]:
        first=0
        for i in range(len(nums)):
            first^=nums[i]
        div=1
        while (div&first)==0:
            div<<=1
        tmp1=0
        tmp2=0
        for i in range(len(nums)):
            if nums[i]&div:
                tmp1^=nums[i]
            else:
                tmp2^=nums[i]
        return [tmp1,tmp2]
