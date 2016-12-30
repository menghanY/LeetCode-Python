# https://leetcode.com/problems/power-of-four/
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
class Solution(object):
    def isPowerOfFour(self, num):
        return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) != 0
