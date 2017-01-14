# https://leetcode.com/problems/unique-binary-search-trees/
class Solution(object):
    def numTrees(self, n):

        dp = [1] * (n+1)
        for i in range(1,n+1):
            ways = 0
            for j in range(1,i+1):
                ways  += dp[j - 1] * dp[i-j]
            dp[i] = ways

        return dp[-1]