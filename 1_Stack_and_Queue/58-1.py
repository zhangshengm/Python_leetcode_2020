#字符串去除首尾空格，以及去除连续的空格
#字符串转列表，列表转字符串
#First answer
class Solution:
    def reverseWords(self, s: str) -> str:
        #去除字符串的首尾空格
        # s1=str.strip()
        #去除字符串的首尾空格以及中间多余空格
        s1=' '.join(s.split())
        #将字符串按空格划分，转换为字符列表
        s1=s1.split(' ')
        s2=[]
        t=len(s1)
        while t>0:
            s2.append(s1.pop())
            t=t-1
        return ' '.join(s2)
#Second answer
class Solution:
    def reverseWords(self, s: str) -> str:
        #删除字符串首尾空格
        s=s.strip()
        #下标值[0,len-1]
        i=j=len(s)-1
        each=[]
        while i>=0:
            #找到首个空格下标
            while i>=0 and s[i]!=' ': i=i-1
            #添加单词
            each.append(s[i+1:j+1])
            #跳过连续的空格
            while s[i]==' ': i=i-1
            j=i
        #拼接字符列表为字符串
        return ' '.join(each)
# Third answer
class Solution:
    def reverseWords(self, s: str) -> str:

        #下标值[0,len-1]
        i=j=len(s)-1
        each=[]
        while i>=0:
            #找到首个非空格元素
            while i>=0 and s[i]==' ': i=i-1
            j=i
            #找到串中间首个空格下标
            while i>=0 and s[i]!=' ': i=i-1
            #添加单词
            #考虑到首部有空格情况
            if j>=0:
               each.append(s[i+1:j+1])
       
        #拼接字符列表为字符串
        return ' '.join(each)
