class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        output = 0
        curr = 0
        i = 0

        for j in nums:
            while j in unique:
                curr -= nums[i]
                unique.remove(nums[i])
                i += 1
            unique.add(j)
            curr += j
            output = max(curr, output)

        return output
