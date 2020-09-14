#need_time为计算出来的小时数，hour为本来的小时数
def deal_day(need_time,hour):
    #计算出来需要加上的天数
    flag=0
    #计算出来的小时
    need_time+=hour
    while need_time >=24:
       flag+=1
       need_time-=24
    return [flag,need_time]

#need_day为计算出来的天数，month为本来的月份
def deal_month(need_day,month):
    #要加的月数
    flag1=0
    d={"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
    t=month
    while need_day>=d.get(t):
          flag1+=1
          need_day-=d.get(t)
          t=str(int(t)+1)
    return [flag1,need_day]
    
s="7.9/8"
t=s.split('/')
#day[0]表示月份7
#day[1]表示日9
day=t[0].split('.')
#表示小时8
time=int(t[1])

#f[0],f[1]为加的天数，和剩下的小时数
f=deal_day(729,time)
print(f)
#g[0],g[1]为加的月数，和剩下的天数
g=deal_month(f[0]+int(day[1]),day[0])
s2=str(int(day[0])+g[0])+"."+str(g[1])+'/'+str(f[1])

print(s2)
