class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>0 else -1
        x = abs(x)
        res = 0
        while x>9:
            res += x%10
            res*=10
            x //= 10
        return (res+x)*sign if -(2**31)<= res<= (2**31)-1 else 0
