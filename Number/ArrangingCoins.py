# https://leetcode.com/problems/arranging-coins/
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
class Solution(object):
    def arrangeCoins1(self, n):
        lineSum = 0
        xline = 0
        while True:
            xline += 1
            lineSum += xline
            if lineSum > n : return xline - 1
    def arrangeCoins2(self, n):
        return int((1 + 8 * n) ** 0.5 - 1) / 2
