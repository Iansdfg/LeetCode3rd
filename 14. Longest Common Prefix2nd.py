class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:return ''
        if len(strs)==1:
            return strs[0]
        strs.sort(key = lambda x:len(x))
        tar = strs[0]
        prfix = ''
        for i in range(len(tar)):
            for strr in strs[1:]:
                if strr[i] != tar[i]:
                    return prfix
            prfix+=strr[i]
            
        return str(prfix)
            
