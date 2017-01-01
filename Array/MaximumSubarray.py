# https://leetcode.com/problems/maximum-subarray/
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray1(self, nums):
        # (containing at least one number)
        sub_sum, max_sum = nums[0], nums[0]
        for val in nums[1:]:
            if sub_sum + val > val:
                sub_sum += val
            else:
                sub_sum = val
            max_sum = max(sub_sum, max_sum)

        return max_sum
    #TLE
    def maxSubArray2(self, nums):
        lenNums = len(nums)
        subArraysSum = []
        for i in range(0,lenNums):
            for j in range(i,lenNums):
                subArraysSum.append(sum(nums[i:j + 1]))
        return max(subArraysSum)






