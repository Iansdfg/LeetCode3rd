class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:return s
        cycle = 2*numRows-2
        section_num = len(s)//cycle
        res = ''
        for row in xrange(numRows):
            section = 0
            for section in xrange(section_num+1):
                if row ==0 or row == numRows-1:
                    if section*cycle+row< len(s):
                        res+=s[section*cycle+row]
                else:
                    if section*cycle+row< len(s):
                        res+=s[section*cycle+row]
                    if (section+1)*cycle-row< len(s):
                        res+=s[(section+1)*cycle-row]
        return res
        
