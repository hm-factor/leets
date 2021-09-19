from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(0, len(nums)):
      n = nums[i]
      m = target - n
      if m in d:
          return [d[m], i]
      else:
          d[n] = i
