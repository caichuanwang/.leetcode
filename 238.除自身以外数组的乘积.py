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
        print(l)
        l[0] = 1
        for i  in range(1,length):
            l[i] = l[i-1] * nums[i-1]
        
        r[length-1] = 1
        for i  in reversed(range(length-1)):
            r[i] = r[i+1] * nums[i+1]
        
        for i  in range(length):
            resp[i] = l[i] * r[i]
            
        return resp
        
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
# @lc code=end

