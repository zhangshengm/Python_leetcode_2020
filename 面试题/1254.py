
class Solution:
    def closedIsland(self, grid):
        #四个方向
        directions=((-1,0),(1,0),(0,1),(0,-1))
        result=0
        height,width=len(grid),len(grid[0])
        for i in range(height):
            for j in range(width):
                #如果该点是岛屿，就将该点放入栈中
                if grid[i][j]==0:
                   #执行过操作就置为1
                   grid[i][j]=1
                   #flag代表是否是封闭岛屿
                   flag,res=True,[]
                   res.append((i,j))
                   while res:
                        #如果在边上就不是封闭岛屿
                        h,w=res.pop()
                        if h==0 or h==height-1 or w==0 or w==width-1:
                           flag=False
                        for x,y in directions:   
                            m,n=h+x,w+y
                            if 0<=m<height and 0<=n<width and grid[m][n]==0:
                               #执行过操作，陆地变成海洋
                               grid[m][n]=1
                               res.append((m,n))
                   if flag:
                       result+=1
        return result
