class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) / 2
            if sum((num - 1) / mid for num in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left

    """
    maxOp = 4
    [2,4,8,2]
    
    l = 1
    r = 4.5
    
    mid = 2.75
    
    12/2.75 > 4
    """
