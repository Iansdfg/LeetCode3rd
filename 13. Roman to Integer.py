class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        for pos,char in enumerate(s):
            res += dic[char]
            if (char == "M" or char == "D") and pos>0 and s[pos-1] == 'C':
                res-=200
            elif (char == "C" or char == "L") and pos>0 and s[pos-1] == 'X':
                res-=20
            elif (char == "X" or char == "V") and pos>0 and s[pos-1] == 'I':
                res-=2
            # print(res)
        return res
                
            
        
