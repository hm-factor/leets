"""
    ABC BAC  0
    ABC BA   1
    ABC BACD 1
    ABC BAKE 2
    AAB BAA  0
    
    AABCD ABCEE

    from the base, keep track of characters not in string2
    from string2, keep track of excess characters
"""


def edit_anagrams(a: str, b: str) -> int:
    # comments are for the 'edit' function which was an additional level of complexity
    # (if a character would be deleted and added, condense into one operation)
    letters = {}
    count = 0
    # pos = 0
    # neg = 0

    for ch in a:
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1
    for ch in b:
        if ch in letters:
            letters[ch] -= 1
        else:
            letters[ch] = -1

    for ch in letters.keys():
        count += abs(letters[ch])
        # if letters[ch] > 0:
        #   pos += 1
        # elif letters[ch] < 0:
        #   neg += 1
        
    return count
    # return max(pos, neg)

print(edit_anagrams("ABC", "ABCC"))