#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sumMax = -float('inf')
        currMax = 1
        currMin = 1
        for i  in range(len(nums)):
            if nums[i] <0 :
                temp = currMax
                currMax = currMin
                currMin = temp
            
            currMax = max(currMax * nums[i],nums[i])
            currMin = min(currMin * nums[i],nums[i])
            sumMax = max(currMax,sumMax)
        
        return sumMax
    
    def maxProduct2(self,nums: list[int]) -> int:
        product = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        for i  in range(1,len(nums)):
            temp = currMax
            currMax = max(max(currMax * nums[i],nums[i]),currMin * nums[i])
            currMin = min(min(temp * nums[i],nums[i]), currMin * nums[i])
            product = max(product,currMax)
        return product
    
    def maxProduct3(self, nums: list[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


s = Solution()
a = s.maxProduct3([-4,-3,-2])
print(a)
# @lc code=end

