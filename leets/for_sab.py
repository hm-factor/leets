"""
  1. recursive binary search
  2. decimal representation of fractions (f strings -> f'str{variables}str')
  3. make two words out of one with every other letter: waists -> wit + ass, board -> bad + or
  4. sums int value of all letters in file
  5. given a list of words, return a dict whose keys are ints and values are words that are that long
  6. given an amount of money, return every different ways that can be represented using coins
"""

def binary_search(nums: list, target: int) -> bool:
  mid = len(nums)//2

  while mid < len(nums):
    if target < nums[mid]:
      return binary_search(nums[0:mid], target)
    elif target > nums[mid]:
      return binary_search(nums[mid + 1:], target)
    elif target == nums[mid]:
      return True
  
  return False

# arr = [1,2,3,4,5,6,7]

# print(binary_search(arr, 4))

def sum_lines(fname: str) -> dict:
  alph = {chr(x+96):x for x in range(1,27)}
  sum = 0
  with open(fname) as f:
    # content = f.read().splitlines()
    for line in f:
      line = line.strip()
      for ch in line:
        if ch != " ":
          sum += alph[ch]
  return sum

# print(sum_lines('./file.txt'))