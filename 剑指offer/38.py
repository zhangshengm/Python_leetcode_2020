class Solution:
    def permutation(self, s: str) -> List[str]:
        sss,res=list(s),[]
        #x是传入已经固定的字符位置
        def DFS(length):
            #代表字符已经遍历完毕
            if length==len(sss)-1:
                res.append(''.join(sss))
                return
            dic=set()
            #首层遍历取所有可能的字符值
            #x代表替换的位置，i代表用第i个字符替换x
            #从length开始表示执行一步该位置保持不变
            for i in range(length,len(sss)):
                #如果同一层有重复的字符，则剪纸，不执行该重复字符
                if sss[i] in dic: continue
                #如果不是重复字符
                dic.add(sss[i])
                #替换当前位置的字符
                sss[length],sss[i]=sss[i],sss[length]
                DFS(length+1)
                #当每次执行结束后，撤销操作，保证sss为最先的字符
                sss[length],sss[i]=sss[i],sss[length]
        DFS(0)
        return res
