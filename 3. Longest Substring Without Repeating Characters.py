class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = dict()
        res = 0
        l = 0
        for r, char in enumerate(s):
            if char in chars:
                l = max(l, chars[char]+1)
            chars[char] = r
            res = max(res, r-l+1)
        return res
