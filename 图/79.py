import copy
class Solution:
    #用BFS搜索时，考虑起点相同，还是不同；层序遍历，若起点只有一个，可以直接剪枝，将搜索过的点设为空
    #由于BFS搜索时，可能某一层节点的下一个节点有重叠，导致某一层的多个节点置为空，能到路径被封死
    def exist(self, board, word):
        #单元格或者搜索的单词为空
        if not word or not board: return False
        #首先确定第一个单词的位置
        res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    res.append([i,j])
        if not res: return False
        flag=False
        # print(res)
        #第一个单词的位置
        
        for ri in res:
            print(ri)
            board1,tmp=copy.deepcopy(board),[ri]
            w_t=1
            # print(board1)
            while tmp:
                t=[]
                print(w_t)
                print(tmp)
                if w_t==len(word):
                    flag=True
                    break
                for t1 in tmp:
                    r,c=t1[0],t1[1]
                    board1[r][c]=" "     
                    if c+1<len(board[0]):
                       if board1[r][c+1] ==word[w_t]:
                              t.append([r,c+1])
                    if r+1<len(board):
                       if board1[r+1][c] ==word[w_t]:
                              t.append([r+1,c])
                    if r-1>=0:
                       if board1[r-1][c] ==word[w_t]:
                              t.append([r-1,c])                      
                    if c-1>=0:
                       if board1[r][c-1] ==word[w_t]:
                              t.append([r,c-1])      
                w_t+=1 
                tmp=t  
            if flag: return True
                  
        return flag

    
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.row,self.col=len(board),len(board[0])
        def DFS(ri,length):
            if length==len(word):
                return True
            r,c=ri[0],ri[1]
            tmp=board[r][c]
            board[r][c]=""
            t=[]
            if r+1<self.row:
               if board[r+1][c]==word[length]:
                  t.append([r+1,c])
            if c+1<self.col:
               if board[r][c+1]==word[length]:
                   t.append([r,c+1])
            if r-1>=0:
               if board[r-1][c]==word[length]:
                   t.append([r-1,c])
            if c-1>=0:
               if board[r][c-1]==word[length]:     
                   t.append([r,c-1])   
            for t1 in t: 
                if DFS(t1,length+1): return True
            board[r][c]=tmp
            
            return False

            

        #单元格或者搜索的单词为空
        if not word or not board: return False
        #首先确定第一个单词的位置
        res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    res.append([i,j])

        for ri in res:
            if DFS(ri,1): return True
        return False




        
   
