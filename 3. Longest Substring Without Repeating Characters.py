class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_pos = dict()
        left = 0
        maxx = 0
        for right, char in enumerate(s):
            if char in char_pos:
                left = max(char_pos[char]+1, left)
            char_pos[char] = right
            maxx = max(maxx, right-left+1)
        return maxx
            

            
