class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s) == 1:
            return 1

        c = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    c += 1
                    print(s[i:j+1])
                    dp[i][j] = True

        return c
        