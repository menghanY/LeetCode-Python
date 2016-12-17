# https://leetcode.com/problems/single-number-iii/
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

class Solution(object):
    def singleNumber1(self, nums):
        numDict = {}
        for num in nums :
            numDict[num] = numDict.get(num,0) + 1
        result = []
        for key in  numDict :
            if numDict[key] == 1 :
                result.append(key)
        return result

    # https: // discuss.leetcode.com / topic / 30166 / easy - python - o - n - o - 1 - solution
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]