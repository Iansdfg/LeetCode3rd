class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        l = 0
        res = 0
        for r, char in enumerate(s):
            if char in dic:
                l = max(dic[char] + 1, l)
            dic[char] = r
            res = max(r-l+1, res)
        return res
            
                
                
