"""
  1. recursive binary search
  2. decimal representation of fractions (f strings -> f'str{variables}str')
  3. make two words out of one with every other letter: waists -> wit + ass, board -> bad + or
  4. sums int value of all letters in file
  5. given a list of words, return a dict whose keys are ints and values are words that are that long
  6. given an amount of money, return every different ways that can be represented using coins
"""


# def binary_search(target, input_list, idx=0):
#     #     mid is middle idx
#     mid = len(input_list)//2

#     print(mid, idx, input_list)

#     while mid < len(input_list):
#         if target > input_list[mid]:
#             return binary_search(target, input_list[mid+1:len(input_list)], idx + mid)
#         elif target < input_list[mid]:
#             return binary_search(target, input_list[0:mid], idx)
#         elif target == input_list[mid]:
#             return idx + mid

#     return "Number not in list"


# arr = [1, 2, 3, 4, 5, 6, 7]
# binary_search(3, arr)

#1
def binary_search(target, input_list, idx=0):
    mid = len(input_list)//2

    if target > input_list[-1]:
        return "Number not in list"

    while mid < len(input_list):
        if target > input_list[mid]:
            return binary_search(target, input_list[mid:len(input_list)], idx + mid)
        elif target < input_list[mid]:
            return binary_search(target, input_list[0:mid], idx)
        elif target == input_list[mid]:
            return idx + mid

    return "Number not in list"


arr = [1, 2, 3, 4, 5, 6, 7]
binary_search(7, arr)

#1
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

#3
def alternade(fname: str) -> str:
  content = None
  with open(fname) as f:
    content = f.read().splitlines()

  for word in content:
    s1 = ""
    s2 = ""
    for i in range(len(word)):
      if i%2 == 0:
        s1 += word[i]
      else:
        s2 += word[i]

    if s1 in content and s2 in content:
      print(f'\"{word}\": makes \"{s1}\" and \"{s2}\"')
    
print(alternade('./words.txt'))

#4
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

#5
def word_lengths(words: list) -> dict:
  output = dict()
  for word in words:
    curr = len(word)
    if curr in output:
      output[curr].append(word)
    else:
      output[curr] = [word]
  return output

# arr = ['ok', 'no', 'thanks', 'pants', 'see', 'goodbye']
# print(word_length(arr))

#6
def make_change(cents: int, total: int) -> int:
  pass
  '''
    create tree that goes through every combination of change
    return 1 if cents achieved, return 0 if sum over cents
  '''
def make_change(target):
    coins = [1, 5, 10, 25, 50, 100]
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    print(ways[target])


make_change(200)

