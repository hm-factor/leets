def moveZerosToEnd(arr):
  for idx in range(len(arr)):
    if arr[idx] == 0:
      pointer = idx + 1
      while pointer < len(arr) and arr[pointer] == 0:
        pointer += 1

      if pointer < len(arr):
        arr[idx], arr[pointer] = arr[pointer], arr[idx]

  return arr
