#快速排序,最好情况，O(n*log(n));最差情况,O(n*n)
def quick_sort(num):
    if len(num)<2: return num
    tmp=num[0]
    left=[i for i in num[1:] if i<tmp ]
    right=[j  for j in num[1:] if j>=tmp]
    return quick_sort(left)+[tmp]+quick_sort(right)


#归并排序, 时间复杂度 O(n*log(n)),空间复杂度 O(n)
def merge_sort(num,tmp,left,right):
    if left>=right: return 
    mid=(left+right)//2
    le=left
    ri=mid+1
    tmp_index=left
    merge_sort(num,tmp,left,mid)
    merge_sort(num,tmp,mid+1,right)

    while le<=mid and ri<=right:
          if num[le]>num[ri]:
             tmp[tmp_index]=num[ri]
             ri+=1
          else:
             tmp[tmp_index]=num[le]
             le+=1
          tmp_index+=1
    if le<=mid:
       tmp[tmp_index:right+1]=num[le:mid+1]
    if ri<=right:
       tmp[tmp_index:right+1]=num[ri:right+1]
    num[left:right+1]=tmp[left:right+1]
num=[1,6,7,8,2,3,4,5,10]
tmp=[0]*len(num)
merge_sort(num,tmp,0,len(num)-1)
print(num)


#小根堆排序:返回k个最小的数，时间复杂度为O(n*log(n))
#父节点的值小于或者等于子节点的值
import heapq
def heapq_sort(num,k):
    if k==0: return []
    t=[]
    for n in num:
        heapq.heappush(t,n)
    return [heapq.heappop(t)  for i in range(k)]
    
#大根堆排序:返回k个最大的数，时间复杂度为O(n*log(n))
#父节点的值大于或者等于子节点的值
def heapq_sort(num,k):
    if k==0: return []
    t=[]
    for n in num:
        heapq.heappush(t,-n)
    return [-heapq.heappop(t)  for i in range(k)]
    
    
#返回k个最小的元素: O（n*log(k)）
t=[]
for n in num:
    if len(t)<k:
       heapq.heappush(t,-n)
    elif len(t)==k:
       heapq.heappushpop(t,-n)
print([-i for i in t])

#返回k个最大的元素:  O（n*log(k)）
t=[]
for n in num:
    if len(t)<k:
       heapq.heappush(t,n)
    elif len(t)==k:
       heapq.heappushpop(t,n)
print([i for i in t])    


k=5
num=[4,3,1,6,7,8,12,56]
t=heapq_sort(num,k)
print(t)

#选择排序，每轮找最小的值，放在最前面，循环遍历
def select_sort(num):
    if not num: return num
    for i in range(len(num)):
        min_index=i
        for j in range(i+1,len(num)):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[i]
    return num

#冒泡排序,两两比较相邻位置，如果反序，则交换位置
def bubble_sort(num):
    if not num: return num
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[j]<num[i]:       
               num[i],num[j]=num[j],num[i]
    return num
