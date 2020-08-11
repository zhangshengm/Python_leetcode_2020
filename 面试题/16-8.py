class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        #分别计算a和b出现的次数
        n_a,n_b,n=0,0,len(value)
        for i in pattern:
                if i=='a':
                    n_a+=1
                else:
                    n_b+=1
        #两个都为空
        if not pattern and not value:
            return True
        #模式为一个字母，字符串为空
        if n_a+n_b==1 and not value:
            return True
        #模式为多个字母，字符串为空
        elif pattern and not value:
            return False
        #模式为空，字符串非空
        elif not pattern and value:
            return False
        #模式和字符串都非空
        else:
            #模式中只有一个字母
            if n_a==0 or n_b==0:
               tmp=max(n_a,n_b)
               if n%tmp!=0:
                  return False
               #每个子串d个字母,n_str中只有一个子串
               d,n_str=n//tmp,set()
               for i in range(tmp):
                   n_str.add(value[i*d:i*d+1])
                   if len(n_str)>1: break
               return len(n_str)==1
            #模式有多个字母
            else:
               #遍历字母a的所有长度
               for i in range(0, n//n_a+1):            # 一般情况
                   #删去a后剩下的字符是否可以被n_b平分吗
                   if (n-i*n_a) % n_b == 0:           # 只判断能整除的情况
                      #每个字母b代表的长度
                      j = (n-i*n_a)//n_b
                      cur, judge1, judge2 = 0, set(), set()
                      for ch in pattern:           # 分别判断两个集合是否有第二种字符串出现
                         if ch == 'a':
                            judge1.add(value[cur:cur + i])
                            cur += i
                         else:
                            judge2.add(value[cur:cur + j])
                            cur += j
                         if len(judge1) > 1 and len(judge2) > 1:
                            break
                      #如果某一个长度使得ab模式匹配
                      if len(judge1) == 1 and len(judge2) == 1:
                         return True                   # 如果两个集合都只有一种字符串，那么就是True
            return False
