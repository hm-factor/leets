class Solution:
    def sequentialDigits(self, low, high):

      # change into str, iterate over and add 1 as you go through
      # keeping track of the previous digit

      # variable keeps track of the previous number, 'while num < high' do all logic

#   Input: low = 100, high = 300
#   Output: [123,234]

#   Input: low = 1000, high = 13000
#   Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

        nums = '123456789'
        out = []
        
        i = len(str(low))
        for j in range(len(nums)):
            curr = int(nums[j:i+j])
            if low <= curr and curr <= high:
                out.append(curr)
            else:
                return out
        return out
