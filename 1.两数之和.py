#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        resp: list[int] = []
        len = nums.__len__()
        for i  in range(len):
            for j  in range(i+1,len):
                if nums[i] + nums[j] == target:
                    resp.append(i)
                    resp.append(j)
        return resp

    # 第二种解法
    def twoSum2(self, nums: list[int],target: int ) -> list[int]:
        resp : list[int] = []
        d = dict()
        for i,v  in enumerate(nums):
            diff = target - v
            if v in d:
                resp.append(i)
                resp.append(d[v])
            else:
                d[diff] = i
        return resp
        
        
        
        
        

s = Solution()
resp = s.twoSum2([1,2,3,4],5)
print(resp)
        
# @lc code=end

