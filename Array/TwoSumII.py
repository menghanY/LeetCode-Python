# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.

class Solution(object):
 # https: // discuss.leetcode.com / topic / 19631 / my - python - o - n - o - 1 - solution
        def twoSum(self, numbers, target):
            left = 0
            right = len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return left + 1, right + 1
            return -1, -1
