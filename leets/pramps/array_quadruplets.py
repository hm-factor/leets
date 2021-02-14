def find_array_quadruplet(arr, s):
  arr.sort()
  idx = 0

  while idx < len(arr) - 3:
    diff = s - arr[idx]
    triple = find_array_triple(arr[idx+1:], diff)
    if len(triple) == 0:
      idx += 1
    else:
      return [arr[idx]] + triple

  return []


def find_array_double(arr, s):
  lower = 0
  upper = len(arr) - 1

  while lower < upper:
    if arr[lower] + arr[upper] < s:
      lower += 1
    elif arr[lower] + arr[upper] > s:
      upper -= 1
    else:
      return [arr[lower], arr[upper]]

  return []


def find_array_triple(arr, s):
  idx = 0

  while idx < len(arr) - 2:
    diff = s - arr[idx]
    double = find_array_double(arr[idx+1:], diff)
    if len(double) == 0:
      idx += 1
    else:
      return [arr[idx]] + double

  return []
