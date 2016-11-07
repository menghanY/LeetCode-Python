class Solution(object):
    def containsDuplicate(self, nums):
        numDict = {}
        for num in nums:
            if numDict.get(num) : return True
            else: numDict[num] = 1
        return False