class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(nums,temp,l,r):
            if l>=r: return 0
            mid=(l+r)//2
            ncount=mergesort(nums,temp,l,mid)+mergesort(nums,temp,mid+1,r)
            left_index=l
            right_index=mid+1
            temp_index=l
            while left_index<=mid and right_index<=r:
                   if nums[left_index]>nums[right_index]:
                        temp[temp_index]=nums[right_index]
                        right_index+=1
                   else: 
                       #当左边元素小于等于右边某个元素时，逆序数目为右边数组[mid+1:right_index]
                         temp[temp_index]=nums[left_index]
                         ncount+=(right_index-mid-1)
                         left_index+=1
                   temp_index+=1
           #temp_index代表当前排好序的临时数组中的最后一个元素
            if left_index<=mid:
               #右边数组全部排序完，左边数组大的值没有排序完
               temp[temp_index:r+1]=nums[left_index:mid+1]
               #逆序数为右边数组长度[mid+1:r+1]*左边剩余元素个数[left_index:mid+1]
               ncount+=((r+1-mid-1)*(mid+1-left_index))
            if right_index<=r:
               temp[temp_index:r+1]=nums[right_index:r+1]
            #保存每个排序好的小块
            nums[l:r+1]=temp[l:r+1]
            return ncount
        tmp=[0]*len(nums)
        return mergesort(nums,tmp,0,len(nums)-1)
