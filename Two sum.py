class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        n = len(nums)
        '''for i in range(n):
            d[nums[i]] = i'''
        for i in range(n):
            if ( target - nums[i]) in d:
                return [d[target - nums[i]],i]
            d[nums[i]]=i
                
        
        
