class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        maxx = ''
        for pos in range(1, len(s)):
            sub = self.check_palindrome(s, pos, pos)
            if len(sub) > len(maxx):
                maxx = sub
            sub = self.check_palindrome(s, pos, pos - 1)
            if len(sub) > len(maxx):
                maxx = sub
        return maxx
            
    def check_palindrome(self, s, r, l):
        while l >= 0 and r < len(s) and s[r] == s[l]:
            r += 1
            l -= 1
        return s[l + 1:r]
        
