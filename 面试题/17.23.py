class Solution:
    # (0,0) (1,1) (0,0)
    # (1,1) (2,2) (0,0)
    # (1,2) (2,3) (0,0)
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return 0
        x,y=len(matrix),len(matrix[0])
    #dp[i][j][0]代表该元素以及上边元素的0连续的个数，dp[i][j][0]代表该元素以及左边元素的0的连续的个数，
        dp=[[[0,0] for _ in range(x+1)] for _ in range(y+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if matrix[i-1][j-1]==0:
                  dp[i][j][0]= dp[i-1][j][0]+1
                  dp[i][j][1]=dp[i][j-1][1]+1
        r,c,size=-1,-1,0
        for i in range(1,x+1):
            for j in range(1,y+1):
                if matrix[i-1][j-1]==0:
                    #取最短的一边
                    t_size=min(dp[i][j])
                    while t_size>size:
                        #判断左边元素的上方的零的个数，判断上方元素左边0的个数
                        if dp[i][j-t_size+1][0]>=t_size and dp[i-t_size+1][j][1]>=t_size:
                            r,c=i-t_size,j-t_size
                            size=t_size
                            break
                        t_size-=1
        if size==0:
            return []
        else:
            return [r,c,size]
