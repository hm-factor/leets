def searchRange(self, nums: List[int], target: int) -> List[int]:
  ans = [-1, -1]
  if not nums or target > nums[-1]:
      return ans

  l, r = 0, len(nums)

  while l < r:
      mid = (l+r)//2
      if target > nums[mid]:
          l = mid+1
      else:
          r = mid
  ans[0] = l if nums[l] == target else -1
  r = len(nums)-1
  while l < r:
      mid = (l+r)//2 + 1
      print(mid)
      if target < nums[mid]:
          r = mid - 1
      else:
          l = mid
  ans[1] = r if nums[r] == target else -1
  return ans
