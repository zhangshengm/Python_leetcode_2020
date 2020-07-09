class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        row_s,row_e=0,len(matrix)-1
        column_s,column_e=0,len(matrix[0])-1
        #保存输出列表
        res=[]
        #从左往右，从上往下，从右往左，从下往上
        while True:
            for i in range(column_s,column_e+1): res.append(matrix[row_s][i])
            row_s+=1
            if row_s>row_e: break
            for j in range(row_s,row_e+1): res.append(matrix[j][column_e])
            column_e-=1
            if column_e<column_s: break
            for k in range(column_e,column_s-1,-1): res.append(matrix[row_e][k])
            row_e-=1
            if row_e<row_s:break
            for l in range(row_e,row_s-1,-1): res.append(matrix[l][column_s])
            column_s+=1
            if column_s>column_e:break
        return res
