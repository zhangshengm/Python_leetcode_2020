class Solution:
    #超时
    def pileBox(self, box: List[List[int]]) -> int:

        if not box: return 0
        L=len(box)
        a=list(range(0,L))
        res=[]
        box.sort(key=lambda x:x[0])
        #保存符合条件的箱子编号
        def true_list(box1,box2):
            res=[]
            for i in box2:
                if box[i][0]-box1[0]>0 and box[i][1]-box1[1]>0 and box[i][2]-box1[2]>0:
                    res.append(i)
            return res
        #tmp_h为当前高度,before_box为局部最高的盒子,tmp_box为符合条件的盒子
        def DFS(tmp_h,before_box,tmp_box):
            if not tmp_box: 
               res.append(tmp_h)
               return
            flag=0
            for i in tmp_box:
                flag+=1
                alist=true_list(box[i],tmp_box)
                DFS(tmp_h+box[i][2],box[i],alist)
            if flag==0:
               res.append(tmp_h)
               return
        DFS(0,[0,0,0],a)
        return max(res)
        
        
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        if not box: return 0
        box.sort()
        dp=[0]*(len(box))
        #dp是包含第i层的最大累加长度，初始化为当前box的高，
        #如果符合条件，dp[i]=max(dp[i],dp[j]+box[i][2])
        for i in range(len(box)):
            dp[i]=box[i][2]
            for j in range(i):
              if box[i][0]>box[j][0] and box[i][1]>box[j][1] and box[i][2]>box[j][2]:
                 dp[i]=max(dp[j]+box[i][2],dp[i])
        return max(dp)
