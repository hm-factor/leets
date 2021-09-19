from typing import List
import math

# dynamic programming solution
# keep track of local maxes as you traverse through list 
# compare to max until through list
# O(n)

def maxSubArray(self, nums: List[int]) -> int:

    n = len(nums)
    l_max = 0
    g_max = -math.inf

    for i in range(0, n):
        l_max = max(nums[i], l_max+nums[i])
        if l_max > g_max:
            g_max = l_max

    return g_max
