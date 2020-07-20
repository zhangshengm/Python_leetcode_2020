class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #把不重复的两个元素分到两个组内,再各自异或
        a,b,k,mask=0,0,0,1
        for n in nums:
            k^=n
        #从右往左找到二进制k中第一个为1的数字，代表两个数字的某位不相同
        # lowbit=x&(～x+1)=x&(−x)
        while (k&mask)==0:
            mask<<=1
        for n in nums:
            if n&mask==0:
                a^=n
            else:
                b^=n
        return [a,b]
