# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution(object):
    # TimeLimitExceeded
    def findDisappearedNumbers1(self, nums):
        totalNums = [val for val in range(1,len(nums) + 1)]
        return [val for val in totalNums if val not in set(nums)]

    # TimeLimitExceeded
    def findDisappearedNumbers2(self, nums):
        out = [] # output list
        for i in range(len(nums)):
            if (i+1) not in nums:
                out.append(i+1)
        return out

    def findDisappearedNumbers3(self, nums):
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))
