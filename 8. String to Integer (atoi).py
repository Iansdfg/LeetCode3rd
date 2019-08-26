class Solution(object):
    def myAtoi(self, strr):
        """
        :type str: str
        :rtype: int
        """
        strr = strr.split()
        if len(strr) == 0:return 0
        s = strr[0]
        sign = 1
        
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-'else 1
            s = s[1:]
        res = 0 
        
        for i in range(len(s)):
            if s[i].isdigit():
                res = res*10 + ord(s[i])-ord('0')
            else:
                break 
                
                
        return max(min(res* sign, 2147483647),-2147483648) 
            
            
