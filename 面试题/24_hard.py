def Compute_two(x,i,j):
    if x=='+':
        return i+j
    elif x=='-':
        return i-j
    elif x=='*':
        return i*j
    elif x=='/':
        return i/j

def Compute_four(num,i,j,k,m,flag):
    for x1 in opt:
        #if flag:
            #continue
        a1=Compute_two(x1, num[i], num[j])
        for x2 in opt:
            #if flag:
                #continue
            a2=Compute_two(x2,a1,num[k])
            for x3 in opt:
                #if flag:
                    #continue
                a3=Compute_two(x3, a2, num[m])
                if a3==24:
                    flag=True
                    #记得输出原始字符
                    print("%s%s%s%s%s%s%s"%(n[i],x1,n[j],x2,n[k],x3,n[m]))
                    break
    return flag
def Select_four(num):
    flag=False
    for i in range(4):
        for j in range(4):
            if i!=j:
                for k in range(4):
                    if k not in [i,j]:
                        Index=[0,1,2,3]
                        Index.remove(i)
                        Index.remove(j)
                        Index.remove(k)
                        m=Index[0]
                        if Compute_four(num,i,j,k,m,flag):
                           flag=True
    if not flag:
        print("NONE")

while True:
    try:
        f,nums=0,[]
        n=input().split()
        dict1={'A':1,'J':11,'Q':12,'K':13}
        opt=['+','*','-','/']
        for i in n:
            if i=="joker" or i=="JOKER":
                f+=1
            elif i in dict1.keys():
                nums.append(dict1[i])
            else:
                nums.append(int(i))
        if f>=1:
            print("ERROR")
        else:
            Select_four(nums)
    except:
           break

