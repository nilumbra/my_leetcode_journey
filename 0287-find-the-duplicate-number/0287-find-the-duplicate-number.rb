# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    nums.each do |num|
        i = num.abs - 1
        # try flip nums[i], but if it's already negative, |nums.abs| must have been used before
        return num.abs if nums[i] < 0 
        nums[i] = -nums[i] # flip
    end
end