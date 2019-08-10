# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s)<2: return s
#         maxx = ''
#         for i in range(1, len(s)):
#             sub = self.findPal(i, i,s)
#             if len(sub)>len(maxx):
#                 maxx = sub
#             sub = self.findPal(i, i-1,s)
#             if len(sub)>len(maxx):
#                 maxx = sub
#         return maxx

    
#     def findPal(self, l,r,s):
#         while l>=0 and r<= len(s)-1 and s[l] == s[r]:
#             l-=1
#             r+=1
#             # print(l,r)
#         return s[l+1:r]
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1: return s
        n = len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start : end + 1]
