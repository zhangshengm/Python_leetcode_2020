while True:
    try:
        n=input()
        res=0
        nums=[]
        for i in range(2,len(n)):
            if n[i] in ['A','B','C','D','E','F']:
                res+=(ord(n[i])-55)*(16**(len(n)-i-1))
            else:
                res+=int(n[i])*(16**(len(n)-i-1))
        print(res)
    except:
        break
