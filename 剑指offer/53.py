class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        if hashmap.get(target):
            return hashmap[target]
        else:
            return 0
