class Solution:
    def hammingWeight(self, n: int) -> int:
        flag=0
        while n:
            #n&1，最右端一位判断，为1时，flag加1
            flag+=n&1
            #n每次向右移动一位，当n全为空时跳出循环
            n>>=1
        return flag
        
