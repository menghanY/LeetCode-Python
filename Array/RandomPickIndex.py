# https://discuss.leetcode.com/topic/59736/several-python-solutions
from collections import defaultdict
from random import randint
class Solution(object):
    def __init__(self, nums):
        self.listnums = defaultdict(list)
        for i in range(len(nums)):
            self.listnums[nums[i]].append(i)
    def pick(self, target):
        index = randint(0,len(self.listnums[target]) - 1)
        return self.listnums[target][index]

