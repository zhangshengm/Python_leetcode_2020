class Solution:
    #python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
    def sumNums(self, n: int) -> int:
        return  n and (n+self.sumNums(n-1))
