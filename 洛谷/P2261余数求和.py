# i     1  2  3  4  5   6   7   8   9   10  11 12
# k//i 10  5  3  2  2   1   1   1   1    1  0  0
# l=1, q=k//i, r=k//q, q*(r-l+1)*(r+l)/2
# n*k-i*k//i, i从1到N
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
