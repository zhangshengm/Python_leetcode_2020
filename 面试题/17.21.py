class Solution:
    def trap(self, height: List[int]) -> int:
        #中低高，或者高低中
        if len(height)<3: return 0
        res=0
        for i in range(1,len(height)-1):
            tmp_left=max(height[:i])
            tmp_right=max(height[i+1:])
            if tmp_left<tmp_right:
               if tmp_left>height[i]:
                  res+=tmp_left-height[i]
            else:
               if  tmp_right>height[i]:
                   res+=tmp_right-height[i]
        return res       
        
                    

class Solution:
    def trap(self, height: List[int]) -> int:
        #中低高，或者高低中
        if not height: return 0
        res=0
        le,ri=0,len(height)-1
        left_max,right_max=height[0],height[ri]
        while le<ri:
            if left_max<=right_max:
                res+=left_max-height[le]
                le+=1
                left_max=max(left_max,height[le])
            else:
                res+=right_max-height[ri]
                ri-=1
                right_max=max(right_max,height[ri])
        return res


