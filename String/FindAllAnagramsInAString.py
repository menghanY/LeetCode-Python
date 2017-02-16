# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        pLen = len(p)
        p_dict = Counter(p)
        res = []
        for i in range(len(s) - pLen + 1):
            if Counter(s[i:i+pLen]) == p_dict:
                res.append(i)
        return res
