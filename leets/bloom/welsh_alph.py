# Enter your code here. Read input from STDIN. Print output to STDOUT
# def order_welsh(words):

#     welsh_alph = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l",
#                   "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]
#     store = {}
#     indices = []

#     for word in words:
#         first_2 = word[:2]
#         if first_2 in welsh_alph:
#             idx = welsh_alph.index(first_2)
#             store[idx] = word
#             indices.append(idx)
#         else:
#             idx = welsh_alph.indx(word[0])
#             store[idx] = word
#             indices.append(idx)

#     indices.sort()
#     output = map(lambda idx: store[idx], indices)
#     return output


def order_welsh(words):

    welsh_alph = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l",
                  "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

    # changes list to dict where key is char and value is idx as a string
    # i could have written the alphabet as a dict, but this takes care of it for me
    welsh_alph_dict = {}
    idx = 0
    for ch in welsh_alph:
        welsh_alph_dict[ch] = str(idx)
        idx += 1

    store = {}
    indices = []

    for word in words:
        code = ""
        i = 0
        while i < len(word):
            double = word[i:i+2]
            if double in welsh_alph_dict:
                code += welsh_alph_dict[double] + ','
                i += 2
            else:
                code += welsh_alph_dict[word[i]] + ','
                i += 1
        indices.append(code)
        store[code] = word

    indices.sort()
    output = list(map(lambda x: store[x], indices))
    return output

    '''
        time-complexity: whichever of O(nlog(n)) or O(n*m) is larger, where n is the number of words 
        and m is the length of the longest word

        space-complexity: O(n) where n is the number of words (if there are more than the number of characters in the alph dict), 
        I will have that many entries in both my store dict and indices list 
    '''
    
    
                
welshes = ["aaa", "chchh", "chhch", "dd"]

print(order_welsh(welshes))


"""
  dd - -> 4
  ddr--> 4, 1
  nah - -> 10, 11
  
  ["3", "3,1", "10,2"]


    check more than initial letter,
    still have to consider 2 char letters

    compound numerical values for later comparison
    store numbers in list
    {
        5: ['dd', 'ddr'],
        15: 'nah',
        4: 'dea',
        10: 'ngah'
    }

    check first two letters of given input word
    compare indices as they appear in the welsh alph list
    store numeric values in dict pointing to words
    sort nums, redefine to words

"""
