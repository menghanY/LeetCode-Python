# https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for index,value in enumerate(nums):
            if value not in d :
                d[value] = index
            else:
                dist = index - d[value]
                if dist <= k:
                    return True
                d[value] = index
        return False
