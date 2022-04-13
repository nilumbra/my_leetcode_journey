# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
    
    nums.sort!.reverse!
    print nums
    (nums.length - 2).times do |idx| 
        if nums[idx] < nums[idx+1] + nums[idx+2] 
            return nums[idx] + nums[idx+1] + nums[idx+2] 
        end
    end
    
    0
end