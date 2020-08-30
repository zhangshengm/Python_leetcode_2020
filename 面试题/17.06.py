class Solution:
    #digit=位数(10)
    #对于2304来说: high=23,cur=0,low=4:
    #对于十位上出现2的范围是: 0020-2229:  0到22共23组，每组10个=high*digit

    #对于2314(cur小于目标值)来说: high=23,cur=1,low=4:
    #对于十位上出现2的范围是: 0020-2229:  0到22共23组，每组10个=high*digit


    #对于2324来说: high=23,cur=2,low=4:
    #对于十位上出现2的范围是: 0020-2324:  分成两个部分：0020-2229和2320-2324
    #                      =high*digit+low+1


    #对于2334(cur大于目标值)来说: high=23,cur=1,low=4:
    #对于十位上出现2的范围是: 0020-2329:  0到23共24组，每组10个=(high+1)*digit
    
    def numberOf2sInRange(self, n: int) -> int:
        digit,res=1,0
        high,cur,low=n//10,n%10,0
        while high!=0 or cur!=0:
              #若high=3,考虑0,10,20，即high个digit
              if cur<2:
                 res+=high*digit
              #目前位为目标值都要考虑低位的影响
              elif cur==2:
                 res+=high*digit+low+1
              else:
                 res+=(high+1)*digit
              low+=cur*digit
              cur=high%10
              high//=10
              digit*=10
        return res
