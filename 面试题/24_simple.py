while True:
    try:
        def DFS(num):
            if len(num)==1:
                return abs(num[0]-24)<error
            for i in range(len(num)):
                for j in range(len(num)):
                    if i!=j:
                        num2=[]
                        for m in range(len(num)):
                            if m!=i and m!=j:
                                num2.append(num[m])
                        for k in range(4):
                            if i>j and k<=1:
                                continue
                            if k==0:
                                num2.append(num[i]+num[j])
                            elif k==1:
                                num2.append(num[i]*num[j])
                            elif k==2:
                                num2.append(num[i]-num[j])
                            elif k==3:
                                if num[j]!=0:
                                    num2.append(num[i]/num[j])
                            #每次操作后就进行下一步递归判断
                            if DFS(num2):
                                return True
                            #记得把新加入的数值删除掉，重新加入数值
                            if num2:
                                num2.pop()
        error=1e-6
        nums=list(map(int,input().split()))
        if DFS(nums):
            print("true")
        else:
            print("false")
    except:
           break
