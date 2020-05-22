class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        else:
            if not matrix[0]:
                return False
        t1=len(matrix)
        t2=len(matrix[0])
        # if t2==0:
        #    return False
        j=t2-1
        s1=[]
        #查找数字所属的行数
        for i in range(t1):
            if matrix[i][j]==target or matrix[i][0]==target:
                return True
            if matrix[i][j]>target and matrix[i][0]<target:
                s1.append(i)
        #遍历符合条件的行数和所有列数
        for t in range(1,j):
            for i in s1:
                if matrix[i][t]==target:
                    return True
        return False    
        
        
        
