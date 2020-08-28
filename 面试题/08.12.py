class Solution:
    #  def DFS(flag,link,row), flag代表上一行元素的[横坐标，纵坐标],link为当前满足的[列数],row为当前行数
    #
    #

    #用res存储每行的列数具体表现为[[2,1,3,4],[1,2,3,4]]
    #如果res为空，不存在这样的列数符合要求；len(res)==1,f=1;len(res)>=2,f=len(res)
    #  在根据每个res子列求得对应的...Q.形式，用单个列表保存，最后添加到最终列表中
    #
    def solveNQueens(self, n: int) -> List[List[str]]:
        #if n==1:
        #   return [["Q"]]
        #记录编号
        res=[]
        #flag为上一行选取的元素坐标,link为满足条件的列坐标，row为当前行行数
        def DFS(flag,link,row):
            #如果符合要求的列数值==n，则找到一条路径
            if len(link)==n:
               res.append(link)
               return
            #如果超出行数，或者link的长度小于行数减一，跳出循环
            if row>n or len(link)<row-1:
                return
            for j in range(1,n+1):
                    #如果列数是重复的，跳过这个值
                    if j in link:
                       continue
                    else:
                       dline=0
                       #[row,j]与之前的元素在一条对角线上，这个值就跳过
                       for k1,v1 in enumerate(link):
                           if abs(j-v1)==abs(row-(k1+1)):
                               dline=1
                       if dline==0:
                          if j==row:
                             DFS([row,j],link+[j],row+1)
                          elif j+row==n+1:
                             DFS([row,j],link+[j],row+1)
                          else:
                             DFS([row,j],link+[j],row+1)
        #遍历第一行的可能列数
        for i in range(1,n+1):
            s=[]
            s.append(i)
            DFS([1,i],s,2)
               
        #求得res的长度
        if len(res)==0:
           return []
        elif len(res)==1:
            flag=1
        else:
            flag=len(res)
            
        #将res每个子列保存为要求的形式输出
        res_q=[]
        for j in range(flag):
            tmp2=[]
            for k in res[j]:
               tmp=""
               for n in range(1,n+1):
                  if n==k:
                     tmp+='Q'
                  else:
                     tmp+='.'
               tmp2.append(tmp)
            # print(tmp2)
            res_q.append(tmp2)
        return res_q
        
