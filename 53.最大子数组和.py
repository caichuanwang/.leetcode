#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = -float('inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum <= 0:
                sum =  0
        return max
    
    def maxSubArray2(self,nums: list[int]) -> int:
        max = nums[0]
        for i  in range(1,len(nums)):
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] += nums[i-1]
            if nums[i] > max:
                max = nums[i]
        return max
    
s = Solution()
a =s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
print(a)

# @lc code=end

