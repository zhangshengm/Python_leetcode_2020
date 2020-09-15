class Solution:
    def closedIsland(self, grid):
        if not grid: return 0
        directions=((1,0),(0,1),(-1,0),(0,-1))
        self.row,self.col=len(grid),len(grid[0])
        res=0
        for i in range(0,self.row-1):
            for j in range(0,self.col-1):    
                if grid[i][j]==0:
                   #假设是封闭岛屿
                   flag=True
                   #走过的陆地不再考虑
                   t,grid[i][j]=[],1
                   t.append([i,j])
                   #保存符合要求的陆地
                   while t:
                      i1,j1=t.pop()
                      #如果在边际上,不是封闭岛屿
                      if i1 in [0,self.row-1] or j1 in [0,self.col-1]:
                               flag=False
                    #   if not flag: continue

                      for k1,k2 in directions:
                          new_i,new_j=k1+i1,k2+j1
                          #坐标有效
                          if 0<=new_j<self.col and 0<=new_i<self.row:
                            #如果是陆地
                             if grid[new_i][new_j]==0:
                                #不在边际上
                                grid[new_i][new_j]=1
                                t.append([new_i,new_j])
                   if flag: res+=1
        return res
       
