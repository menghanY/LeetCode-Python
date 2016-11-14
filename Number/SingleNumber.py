class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1 : return nums[0];
        x = 0
        for i in nums:
            x ^= i
        return x
s = Solution()
print(s.singleNumber([1,0,1]))