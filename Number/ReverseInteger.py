# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
class Solution(object):
    def reverse(self, x):
        if x < 0 : return -self.reverse(-x)
        result = 0
        while x:
            result = x % 10 + result * 10
            x = x // 10
        return result if abs(result)< 2147483648 else 0

s = Solution()