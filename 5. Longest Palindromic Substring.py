class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2: return s
        maxx = ''
        for i in range(1, len(s)):
            sub = self.findPal(i, i,s)
            if len(sub)>len(maxx):
                maxx = sub
            sub = self.findPal(i, i-1,s)
            if len(sub)>len(maxx):
                maxx = sub
        return maxx

    
    def findPal(self, l,r,s):
        while l>=0 and r<= len(s)-1 and s[l] == s[r]:
            l-=1
            r+=1
            # print(l,r)
        return s[l+1:r]
        
