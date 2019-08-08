class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.split()
        if len(str)==0: return 0
        s=str[0]
        i=0
        sign=1
        if s[0]=='-' or s[0]=='+':
            sign=-1 if s[0]=='-' else 1
            i+=1  
        res=0
        while i<len(s):
            if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
                break
            else:
                res=res*10+ord(s[i])-ord('0')
            i+=1
        return max(min(res* sign, 2147483647),-2147483648) 
