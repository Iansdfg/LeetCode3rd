class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for pos, num in enumerate(nums):
            l,r = pos+1, len(nums)-1
            if pos > 0 and nums[pos] == nums[pos-1]:
                continue
            while l<r:
                summ = num+nums[l]+nums[r]
                if summ == 0:
                    res.append([num,nums[l],nums[r]])
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l<r and nums[r-1] == nums[r]:
                        r-=1  
                    l+=1
                    r-=1
                elif summ < 0:
                    l+=1
                elif summ > 0:
                    r-=1
        return res
                
        
