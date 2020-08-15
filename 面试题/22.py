class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def DFS(tmp,left,right,n):
            if len(tmp)==2*n:
               res.append(tmp)
               return
            #括号成对，下一个一定是左括号
            if left==right:
               DFS(tmp+'(',left+1,right,n)
            elif left>right: 
                if left<n:
                   DFS(tmp+'(',left+1,right,n)
                   DFS(tmp+')',left,right+1,n)
                elif left==n:
                   DFS(tmp+')',left,right+1,n)
                else:
                    return 
            else:
                return 

        DFS('(',1,0,n)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def DFS(tmp,left,right,n):
            if len(tmp)==2*n:
               res.append(tmp)
               return
            #括号成对，下一个一定是左括号
            if left==right:
               DFS(tmp+'(',left+1,right,n)
            elif left>right: 
                if left<n:
                   DFS(tmp+'(',left+1,right,n)
                   DFS(tmp+')',left,right+1,n)
                elif left==n:
                   DFS(tmp+')',left,right+1,n)

        DFS('(',1,0,n)
        return res
