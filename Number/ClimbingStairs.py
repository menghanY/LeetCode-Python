class Solution(object):
    def climbStairs(self, n):
        if n <= 2: return n
        numN_1 = 2
        numN_2 = 1
        result = 0
        for x in range(3,n + 1) :
            result = numN_1 + numN_2
            numN_2 = numN_1
            numN_1 = result
        return result
