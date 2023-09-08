# @param {Integer[]} nums
# @return {Boolean}
def is_good(nums)
   n = nums.size
   nums.sort!
   # sort nums and check
   # 1. every number less than n appears once
   # 2. n - 1 appears twice
   for i in (1..n-2) do 
      if i != nums[i-1]
         return false
      end
   end
   
   # if the last two 
   nums[-1] == n-1 && nums[-2] == n-1
end