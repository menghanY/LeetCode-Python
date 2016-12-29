class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
    def majorityElement2(self, nums):
        numCountDict = {}
        lenNumsHalf = len(nums) // 2
        for num in nums :
            numCountDict[num] = numCountDict.get(num,0) + 1
            if numCountDict[num] > lenNumsHalf // 2 :
                return num