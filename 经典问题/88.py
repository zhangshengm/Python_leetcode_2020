class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1=nums1[:m]
        nums1[:]=[]
        i,j=0,0
        while i <m and j<n:
              if copy1[i]>nums2[j]:
                 nums1.append(nums2[j])
                 j+=1
              else:
                nums1.append(copy1[i])
                i+=1
        if i <m:
            for t in copy1[i:m]:
               nums1.append(t)

        if j<n:
            for t in nums2[j:n]:
              nums1.append(t)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1=nums1[:m]
        nums1[:]=[]
        i,j=0,0
        while i <m and j<n:
              if copy1[i]>nums2[j]:
                 nums1.append(nums2[j])
                 j+=1
              else:
                nums1.append(copy1[i])
                i+=1
        if i <m:
            nums1[i+j:]=copy1[i:m]
             

        if j<n:
             nums1[i+j:]=nums2[j:n]
       
