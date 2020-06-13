    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#'+s, '#'+p
        m, n = len(s), len(p)
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        
        for i in range(m):
            for j in range(1, n):
     #以空字符匹配p的前j个字符，j>1保证的是*前面必有字符或.,dp[i][j-2]奇数和偶数项相互影响，因为*前有字母或符号
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j-2]
                #两个字母匹配
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i-1][j-1]
                #j>1保证的是*前面必有字符或., dp[i][j-2]奇数和偶数项相互影响，
                # p[j-1] in [s[i], '.']判断p的前一个字符是否与s[i]相等，
                # dp[i-1][j]判断*之前的p的字符与s的字符是否相等
                elif p[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j-2] or p[j-1] in [s[i], '.'] and dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
