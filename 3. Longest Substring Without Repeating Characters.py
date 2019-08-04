class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        l, res = 0,0
        for r, val in enumerate(s):
            if val in dic:
                l = max(dic[val]+1,l)
            dic[val] = r
            res = max(res, r-l+1)
        return res
