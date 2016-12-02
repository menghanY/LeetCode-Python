# https://leetcode.com/problems/merge-sorted-array/
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# https://discuss.leetcode.com/topic/19513/beautiful-python-solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

