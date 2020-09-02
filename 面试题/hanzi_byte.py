while True:
    try:
        n,len_n=input().split()
        len_n=int(len_n)
        res,tmp=0,""
        for i in n:
                #判断是否是汉字
                if '\u4e00' <= i <= '\u9fff':
                    res+=2
                else:
                    res+=1
                if res<=len_n:
                    tmp+=''.join(i)
        print(tmp)
    except:
        break

while True:
    try:
        n,len_n=input().split()
        len_n=int(len_n)
        if n[len(n)-1].isalpha():
            print(n[:len_n])
        else:
            print(n[:len_n-1])
    except:
        break
