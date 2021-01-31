def flatten_dictionary(dictionary):
  out = {}
  flat("", dictionary, out)
  return out


def flat(string, dictionary, out):
  for k in dictionary.keys():
    temp = string
    if temp == "":
      temp = k
    elif k:
      temp = string + '.' + k

    if isinstance(dictionary[k], dict):
      flat(temp, dictionary[k], out)
    else:
      # temp = temp[1:]
      # removes first element of string
      out[temp] = dictionary[k]
