class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key = len)
        res = ''
        if len(strs)==0:return ''
        stander = strs[0]
        for pos,char in enumerate(stander):
            for i in range(1,len(strs)):
                if strs[i][pos]!=char:
                    return res
            res+=char
        return res
