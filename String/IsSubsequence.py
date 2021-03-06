# https://leetcode.com/problems/is-subsequence/
# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
class Solution(object):
    # https: // discuss.leetcode.com / topic / 57076 / python - simple - solution / 2
    def isSubsequence(self, s, t):
        if len(s) == 0 : return True
        if len(t) == 0 : return False
        i,j = 0,0
        while i < len(s) and j < len(t) :
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)