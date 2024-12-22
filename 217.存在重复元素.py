#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = dict()
        for v in nums:
            if v in d:
                return True
            else:
                d[v] = None
        return False


    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)

s = Solution()
print(s.containsDuplicate([1,2,3,4]))
# @lc code=end

