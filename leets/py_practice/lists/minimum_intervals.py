from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(num - median) for num in nums)


        # cool solution:

        # nums.sort()
        # return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))


        # avg = sum(nums)//len(nums)
        # count = 0
        # for num in nums:
        #     count += abs(num - avg)

        # return count
