# https://leetcode.com/problems/integer-break/
# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
from functools import reduce
class Solution(object):
    # https://discuss.leetcode.com/topic/51597/python-solution-40ms-with-explanation
    def integerBreak(self, n):
        if n == 2 : return 1
        if n == 3 : return 2
        list_3 = [3] * (n // 3)
        mod_3 = n % 3
        if mod_3 == 1 :
            list_3[0] += 1
        if mod_3 == 2 :
            list_3.append(2)
        return reduce(lambda a, b: a * b, list_3)