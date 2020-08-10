class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        #如果两个矩形重叠，只计算一个面积
        if A==E and B==F and C==G and D==H:
            return int((D-B)*(C-A))
        #分别表示横坐标和纵坐标
        X=[A,C,E,G]
        Y=[B,D,F,H]
        #左右下上
        M=[[A,C,B,D],[E,G,F,H]]
        #加入不重复的点
        S=set()
        for x in X:
            for y in Y:
                flag1,flag2=0,0
                for i in range(2):
                    if x>=M[i][0] and x<M[i][1] and  y>M[i][2] and y<=M[i][3]:
                       flag1+=1
                    if x>M[i][0] and x<=M[i][1] and  y>=M[i][2] and y<M[i][3]:
                       flag2+=1
                if flag1==2 or flag2==2:
                   S.add((x,y))
        #两个矩形不重叠
        if not S:
           return  int((C-A)*(D-B)+(G-E)*(H-F))
        #两个矩形重叠
        else:
           S=list(S)
           t1=max(S[0][0],S[1][0])-min(S[0][0],S[1][0])
           t2=max(S[0][1],S[1][1])-min(S[0][1],S[1][1])
           return int((C-A)*(D-B)+(G-E)*(H-F)-t1*t2)
