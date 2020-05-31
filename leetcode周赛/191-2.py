import math
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        def max_v(hori):
            t,s1=0,[]
            for i in range (len(hori)-1):
                j=i+1
                t=hori[j]-hori[i]
                if not s1:
                    s1.append(t)
                if t >s1[-1]:
                    s1.pop()
                    s1.append(t)    
            return s1[-1]
            
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        h_list=horizontalCuts.sort()
        v_list= verticalCuts.sort()
        h_max=max_v(horizontalCuts)
        v_max=max_v(verticalCuts)
        result=int((h_max*v_max)%(math.pow(10,9)+7))
        return result
        
  class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hm,wm=0,0
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in range(len(horizontalCuts)-1):
            hm=max(hm,horizontalCuts[i+1]-horizontalCuts[i])
        for j in range(len( verticalCuts)-1):
            wm=max(wm, verticalCuts[j+1]- verticalCuts[j])

        result=int((hm*wm)%(10**9+7))
        return result
 
