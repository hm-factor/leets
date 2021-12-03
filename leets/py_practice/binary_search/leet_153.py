def findMin(self, nums: List[int]) -> int:
  if not nums:
      return -1

  l, r = 0, len(nums)-1
  while l <= r:
      m = (l+r)//2
      if len(nums) == 1:
          return nums[0]
      if nums[l] < nums[r]:
          return nums[l]
      if nums[m] > nums[m + 1]:
          return nums[m+1]
      if nums[m] < nums[l]:
          r = m
      else:
          l = m
  return -1
