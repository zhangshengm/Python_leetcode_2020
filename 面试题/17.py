class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={}
        d['2']="abc"
        d['3']="def"
        d['4']="ghi"
        d['5']="jkl"
        d['6']="mno"
        d['7']="pqrs"
        d['8']="tuv"
        d['9']="wxyz"
        # for j in d[digits[0]]:
        #     print(j)
        L=len(digits)
        res=[]
        def DFS(i,tmp):
            if i>=L:
               res.append(tmp)
               return
            for ss in d[digits[i]]:
                DFS(i+1,tmp+ss)
        DFS(0,"")
        return res
