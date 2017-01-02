# https://leetcode.com/problems/circular-array-loop/
# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.
from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        mp = defaultdict(lambda: 0)
        for i in A:
            for j in B:
                sm = i + j
                mp[sm] += 1

        res = 0
        for i in C:
            for j in D:
                res += mp[-1 * (i + j)]
        return res

Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2])