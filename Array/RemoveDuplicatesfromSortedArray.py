# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

# https://discuss.leetcode.com/topic/68445/python-with-two-pointers
class Solution(object):
    def removeDuplicates(self, nums):
        originLen = len(nums)
        if originLen == 0 : return 0

        i,j = 1,1
        while i < originLen :
            if nums[i] != nums[i - 1] :
                nums[j] = nums[i]
                j += 1
            i += 1
        nums = nums[:j]
        return j