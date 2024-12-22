#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max:int = 0
        l:int = prices.__len__()
        for i in range(0,l-1):
            for j in range(i+1,l):
                diff:int = prices[j] - prices[i] 
                if diff > max:
                    max = diff
        return max
    
    def maxProfit2(self,prices: list[int]) -> int:
        min:int = 0
        max:int =0
        for i,v  in enumerate(prices):
            if i == 0:
                min = v
                continue
            if v - min > max:
                max = v - min
            if v - min < 0:
                min = v
        return max
        
        
        
        
        
        
         
s:Solution = Solution()
m:int = s.maxProfit2([2,4,2,6,1,8])
print(m)
    
        
# @lc code=end

# class TestMaxProfit(unittest.TestCase):
#     def test_large_input(self):
#         prices = [i for i in range(10000)]
#         s = Solution()
#         result = s.maxProfit(prices)
#         self.assertEqual(result, 9999)

# if __name__ == '__main__':
#     unittest.main()
