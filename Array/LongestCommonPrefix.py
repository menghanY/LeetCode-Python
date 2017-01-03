# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        strs.sort()
        ret = ''
        for k, v in enumerate(strs[0]):
            if v == strs[len(strs) - 1][k]:
                ret += v
            else:
                break
        return ret