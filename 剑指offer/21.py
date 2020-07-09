class Solution:
    # 时间复杂度: O(n)
    #空间复杂度: O(n)
    def exchange(self, nums: List[int]) -> List[int]:
        t1,t2=[],[]
        for i in nums:
            if i%2!=0:
                t1.append(i)
            else:
                t2.append(i)
        return t1+t2
