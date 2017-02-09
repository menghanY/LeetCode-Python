# https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        # https://discuss.leetcode.com/topic/36160/python-o-n-1-pass-in-place-solution-with-explanation/2
        red,head,tail = 0,0,len(nums) - 1
        while head <= tail:
            if nums[head] == 0 :
                nums[red],nums[head] = nums[head],nums[red]
                head += 1
                red += 1
            elif nums[head] == 1:
                head += 1
            else:
                nums[head],nums[tail] = nums[tail],nums[head]
                tail -= 1


# print(Solution().sortColors([0]))
