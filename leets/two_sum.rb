# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    output = []
    
    nums.each_with_index do |n, i|
        diff = target - n
        diff_i = nums.index(diff)
        
         if ((nums.include?(diff)) && (i != diff_i))
             output.push(i, diff_i)
             return output
         end
        
    end
end