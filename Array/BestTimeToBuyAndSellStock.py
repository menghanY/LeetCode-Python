# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self,prices):
        # https://discuss.leetcode.com/topic/78001/python-solution-with-detailed-explanation
        buy,profit = prices[0] if len(prices) else -1,0
        for i in range(1,len(prices)):
            profit = max(profit,prices[i] - buy)
            buy = min(buy,prices[i])
        return profit