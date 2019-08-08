class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        temp = x
        res = 0
        while temp:
            res=res*10+ temp%10
            temp//=10
        return x == res
            
        
