
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s1=['a','e','i','o','u']
        res = cur = 0
        for i in range(len(s)):
            #统计首个滑动字符串的元音字母个数，
            if s[i] in s1:
                cur += 1
            #超出
            if i >= k:
                cur -= s[i-k] in s1
            #以前的最大值和当前滑动窗口内的最大值作比较
            res = max (res,cur)
        return res
