class Solution:
    def permutation(self, S: str) -> List[str]:
        res=[]
        def DFS(tmp,newS):
            if len(tmp)==len(S):
               res.append(tmp)
               return
            h=set()
            for i in range(len(newS)):
                if newS[i] not in h:
                   h.add(newS[i])
                   DFS(tmp+newS[i],newS[0:i]+newS[i+1:])
        DFS("",S)
        # res=set(res)
        return res
