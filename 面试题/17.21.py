class Solution:
    def trap(self, height: List[int]) -> int:
        #中低高，或者高低中
        if len(height)<3: return 0
        res=0
        for i in range(1,len(height)-1):
            if max(height[:i])<max(height[i+1:]):
               if max(height[:i])>height[i]:
                  res+=max(height[:i])-height[i]
            else:
               if  max(height[i+1:])>height[i]:
                   res+=max(height[i+1:])-height[i]
        return res       




