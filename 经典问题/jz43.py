class Solution:
    def countDigitOne(self, n: int) -> int:
        high,now,low=n//10,n%10,0
        digit,res=1,0
        while high or now:
            if now ==0:
                res+=high*digit
            elif now==1:
               res+=high*digit+low+1
            else:
               res+=(high+1)*digit
            low+=now*digit
            now=high%10
            high//=10
            digit*=10
        return res
