from typing import List


def maxSubArray(self, nums: List[int]) -> int:
  if len(nums) == 1:
      return nums[0]

  curr_sum = sum(nums)
  max_sum = curr_sum

  while len(nums) > 0:
      low = nums[0]
      high = nums[-1]
      tmp = max(low, high)

      if tmp == low:
          curr_sum -= high
          nums = nums[:-1]
      else:
          curr_sum -= low
          nums = nums[1:]
      max_sum = max(max_sum, curr_sum)
  return max_sum
