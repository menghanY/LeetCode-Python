
import sys
class Solution(object):
    def thirdMax1(self, nums):
        # https: // discuss.leetcode.com / topic / 64696 / a - python - amusing - solution - which - actually - beats - 98 / 3
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

    def thirdMax2(self, nums):
        nums = set(nums)
        max = max2 = max3 = -sys.maxsize - 1
        for n in nums:
            if n > max:

                max, max2, max3 = n, max, max2

            elif n > max2:

                max2, max3 = n, max2

            elif n > max:

                max3 = n
                
        return max3 if max3 != -sys.maxsize - 1 else max



s = Solution([n])

