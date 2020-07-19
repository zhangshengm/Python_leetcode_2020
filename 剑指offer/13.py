class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def DFS(i,j):
            #如果超出范围,或者数位和大于k值,或者该点之前访问过
            if i>=m or j>=n or sumvalue(i,j)>k or (i,j) in visited: return 0
            #将该点放入参观过后的集合中
            visited.add((i,j))
            res=1+DFS(i+1,j)+DFS(i,j+1)
            return res
        def sumvalue(m,n):
            t=0
            while m or n:
                t+=(m%10+n%10)
                m=m//10
                n=n//10
            return t
        #代表记录的总格数
        flag=0
        visited=set()
        flag+=DFS(0,0)
                    
        return flag
