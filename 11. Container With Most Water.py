class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0 
        l,r = 0,len(height)-1
        while l<r:
            cap = (r-l)*min(height[r],height[l])
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
            res = max(cap,res)
        return res
            
