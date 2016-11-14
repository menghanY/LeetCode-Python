# https://leetcode.com/problems/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Subscribe to see which companies asked this question
class Solution(object):

    def climbStairs1(self, n):
        if n <= 2: return n
        numN_1 = 2
        numN_2 = 1
        result = 0
        for x in range(3,n + 1) :
            result = numN_1 + numN_2
            numN_2 = numN_1
            numN_1 = result
        return result
    
    def climbStairs2(self,n):
        dp = {0:1,1:1}
        for x in range(2,n + 1) :
            dp[x%2] = dp[0] + dp[1]
        return dp[n % 2]
