class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            #每一次找寻过程中，超出寻找的边界或者当前值不为匹配字符
            if not 0<=i <m or not 0<=j<n or board[i][j]!=word[k]: return False
            #如果匹配所有字符,匹配成功
            if k==len(word)-1: return True
            #当前值为匹配字符，则将当前值置为不可用
            tmp,board[i][j]=board[i][j],'/'
            res=dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            #将当前值还原
            board[i][j]=tmp
            return res
        m,n=len(board),len(board[0])
        # dfs[i,j,0]
        #从所有起点进入，如果返回为True代表找到一条路径
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0): return True
        return  False
