class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(num - median) for num in nums)
        
        # avg = sum(nums)//len(nums)
        # count = 0
        # for num in nums:
        #     count += abs(num - avg)

        # return count
