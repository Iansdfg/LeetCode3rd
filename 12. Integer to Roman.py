class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        while num:
            if num>=1000:
                res+='M'
                num-=1000
            elif 900<=num<1000:
                res+='CM'
                num-=900
            elif 900>num>=500:
                res+='D'
                num-=500
            elif 400<=num<500:
                res+='CD'
                num-=400
            elif 400>num>=100:
                res+='C'
                num-=100
            elif 90<=num<100:
                res+='XC'
                num-=90
            elif 90>num>=50:
                res+='L'
                num-=50
            elif 40<=num<50:
                res+='XL'
                num-=40
            elif 40>num>=10:
                res+='X'
                num-=10
            elif 9<=num<10:
                res+='IX'
                num-=9
            elif 9>num>=5:
                res+='V'
                num-=5
            elif 4<=num<5:
                res+='IV'
                num-=4
            elif 4>num>=1:
                res+='I'
                num-=1
        return res
                
            
            
