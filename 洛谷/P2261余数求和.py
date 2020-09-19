
import datetime
start=datetime.datetime.now()
N=10
k=5
res1=0
for i in range(1,N+1):
    res1+=k%i
print(res1)

i=1
res=0
while i<=N:
    q=k//i
    if q==0: break
    r=min(k//q,N)
    res+=q*(r-i+1)*(r+i)/2
    i=r+1

print(int(N*k-res))
end=datetime.datetime.now()
print(end-start)
