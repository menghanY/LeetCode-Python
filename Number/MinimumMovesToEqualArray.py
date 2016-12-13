# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
class Solution(object):
    # https: // discuss.leetcode.com / topic / 66759 / four - python - solutions with-detailed - explanation
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        c = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            c += nums[i] - nums[0]
        return c