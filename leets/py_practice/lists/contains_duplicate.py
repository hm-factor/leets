# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.

from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
  l1 = len(nums)
  l2 = len(set(nums))
  return not (l1 == l2)
