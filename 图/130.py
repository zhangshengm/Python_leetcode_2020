class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #深度优先遍历，尽量让参数为单个坐标，如果为多个坐标，就相当于多了一层for循环
        def DFS(start):
            i,j=start[0],start[1]
            visited[i][j]=1
            for k,m in directions:
                    new_i,new_j=i+k,j+m
                    if  0<=new_i<self.row and 0<=new_j<self.col and not visited[new_i][new_j]:
                        if board[new_i][new_j]=="O" :
                            DFS([new_i,new_j])

        if not board: return
        self.row,self.col=len(board),len(board[0])
        visited=[[0]*self.col for _ in range(self.row)]
        directions=((1,0),(0,1),(-1,0),(0,-1))
 
        for j in range(self.col):
            if board[0][j]=="O" and not visited[0][j]:
               DFS([0,j])
            if board[self.row-1][j]=="O" and not visited[self.row-1][j]:
               DFS([self.row-1,j])
            
        for i in range(self.row):
            if board[i][0]=="O" and not visited[i][0]:
               DFS([i,0])
            if board[i][self.col-1]=="O" and not visited[i][self.col-1]:
               DFS([i,self.col-1])

        for x in range(len(visited)):
            for y in range(len(visited[0])):
                  if visited[x][y]==0:
                      board[x][y]="X"
