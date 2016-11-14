class Solution(object):
    def moveZeroes(self, nums):
        totalZeros = 0
        for i in range(len(nums)):
            if nums[i] == 0 :
                totalZeros += 1
                continue
            nums[i - totalZeros] = nums[i]
            if(totalZeros) : nums[i] = 0
