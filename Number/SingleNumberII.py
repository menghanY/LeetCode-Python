# https://leetcode.com/problems/single-number-ii/
# Given an array of integers, every element appears three times except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
       beforeLen = len(nums)
       if beforeLen < 3: return nums[0]
       setNums = set(nums)
       afterLen = len(setNums)
       return (sum(setNums) * 3 -  sum(nums)) // (3 * afterLen - beforeLen)

s = Solution()
print(s.singleNumber([2,2,2,3,3]))