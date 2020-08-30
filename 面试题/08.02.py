class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        def DFS(x,y,tmp):
            #走到终点
          if not res:
            if x==r and y==c:
               res.append(tmp)
               return 
            #半路中，无路可走了
            elif x<r and y<c:
                if  obstacleGrid[x+1][y]==1 and obstacleGrid[x][y+1]==1:
                    return
                else:
                   #可以向右
                    if y+1<=c and x<=r and obstacleGrid[x][y+1]==0:
                        obstacleGrid[x][y+1]=1
                        DFS(x,y+1,tmp+[[x,y+1]])
                   #可以向下   
                    if x+1<=r and y<=c and obstacleGrid[x+1][y]==0:
                         obstacleGrid[x+1][y]=1
                         DFS(x+1,y,tmp+[[x+1,y]])

            #走到了最下面，右边无路了
            elif x==r and y<c:
                if obstacleGrid[x][y+1]==1:
                    return
                else:
                    if y+1<=c and x<=r:
                       obstacleGrid[x][y+1]=1
                       DFS(x,y+1,tmp+[[x,y+1]])

            #走到了最右边，下面无路了
            elif y==c and x<r:
                if obstacleGrid[x+1][y]==1:
                    return
                else:
                    if x+1<=r and y<=c:
                        obstacleGrid[x+1][y]=1
                        DFS(x+1,y,tmp+[[x+1,y]])
      
        if not obstacleGrid: return []
        res=[]
        r=len(obstacleGrid)-1
        c=len(obstacleGrid[0])-1
     
        if obstacleGrid[0][0]==1:
            return []
        else:
            DFS(0,0,[[0,0]])           
            if not res:
                return []
            else:
                return res[0]

                
