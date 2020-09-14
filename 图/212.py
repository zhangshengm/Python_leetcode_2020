import copy
class Solution:
    #倒数第三个用例没过
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.row,self.col=len(board),len(board[0])
        def DFS(ri,length,k):
            if length==len(words[k]):
                return True
            r,c=ri[0],ri[1]
            tmp=self.board[r][c]
            self.board[r][c]=""
            t=[]
            if r+1<self.row:
               if self.board[r+1][c]==words[k][length]:
                  t.append([r+1,c])
            if c+1<self.col:
               if self.board[r][c+1]==words[k][length]:
                   t.append([r,c+1])
            if r-1>=0:
               if self.board[r-1][c]==words[k][length]:
                   t.append([r-1,c])
            if c-1>=0:
               if self.board[r][c-1]==words[k][length]:     
                   t.append([r,c-1])   
            for t1 in t: 
                if DFS(t1,length+1,k): return True
            self.board[r][c]=tmp
            
            return False


        #单元格或者搜索的单词为空
        if not words or not board: return []
        #首先确定每个单词第一个字母的位置
        res=collections.defaultdict(list)
        result=[]
        for k in range(len(words)):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==words[k][0]:
                        res[k].append([i,j])
        # print(res)
        for k in res.keys():
           for ri in res[k]:
               self.board=copy.deepcopy(board)
               if DFS(ri,1,k): 

                   result.append(words[k])
                   break
        return result
