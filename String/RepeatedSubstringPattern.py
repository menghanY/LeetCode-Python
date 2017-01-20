# https://leetcode.com/problems/repeated-substring-pattern/
class Solution(object):
    def repeatedSubstringPattern(self, str):
        return str in (2 * str)[1:-1]
