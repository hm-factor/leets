def decrypt(word):
  decoded = ""

  if len(word) == 0:
    return decoded

  prev = None

  for i in range(len(word)):
    if i == 0:
      prev = ord(word[i])
      char = chr(prev - 1)
      decoded += char
    else:
      temp = ord(word[i])-prev
      # temp = ascii(char[i])
      while temp < ord('a'):
        temp += 26
      decoded += chr(temp)
      prev = temp+prev

  return decoded
