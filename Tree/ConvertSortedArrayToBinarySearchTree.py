# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from TreeNode import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums : return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        mid = TreeNode(nums[n // 2])
        mid.left = self.sortedArrayToBST(nums[:n // 2])
        mid.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        return mid