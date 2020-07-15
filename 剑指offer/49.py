class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d2,d3,d5=0,0,0
        res=1
        #将丑数按顺序依次存入result数组
        result=[1]*n
        while res<n:
              #局部最小值由之前的丑数互相组合而成
              result[res]=min(result[d2]*2,result[d3]*3,result[d5]*5)
              if result[res]==result[d2]*2:
                  d2+=1
              if result[res]==result[d3]*3:
                  d3+=1
              if result[res]==result[d5]*5:
                  d5+=1    

              res+=1
        return result[res-1]
