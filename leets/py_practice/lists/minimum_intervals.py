class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        avg = sum(nums)//len(nums)
        count = 0
        for num in nums:
            count += abs(num - avg)

        return count
