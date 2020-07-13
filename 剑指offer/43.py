class Solution:
    def countDigitOne(self, n: int) -> int:
        digit,res=1,0
        #高位，目前位，低位
        high,cur,low=n//10,n%10,0
        #当high为0,cur=最高位时，更新cur后，high与cur均为0,跳出循环
        while high!=0 or cur!=0:
              if cur==0:
                  res+=high*digit
              elif cur==1:
                  res+=high*digit+low+1
              else:
                  res+=(high+1)*digit
              low+=cur*digit
              cur=high%10
              high=high//10
              digit*=10
        return res
              
