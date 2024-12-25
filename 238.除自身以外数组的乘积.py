#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length:int = nums.__len__()
        l:list[int] = [None] * length
        r: list[int] = [None] * length
        resp: list[int] = [None] * length
        
        l[0] = 1 
        for i in range(1,length):
            l[i] = l[i-1] * nums[i-1]
        
        r[length-1] = 1
        for i  in reversed(range(length -1)):
            r[i] = r[i+1] * nums[i+1]
            
        for i  in range(length):
            resp[i] = l[i] * r[i]
        
        return resp
    
    # 解法二
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        length = len(nums)
        resp: list[int] = [1] * length
        i,j = 0,length-1
        left,right = 1,1
        while i<= length - 1 and j >= 0:
            resp[i] *= left
            resp[j] *= right
            left *= nums[i]
            right *= nums[j]
            i += 1
            j -= 1
        return resp
        
        
        
s = Solution()
print(s.productExceptSelf2([1,2,3,4]))
# @lc code=end

