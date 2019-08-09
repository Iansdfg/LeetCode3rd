class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '': return 0
        needle_lens = len(needle)
        for i in range(len(haystack)-needle_lens+1):
            if haystack[i:i+needle_lens] == needle:
                return i
        return -1
