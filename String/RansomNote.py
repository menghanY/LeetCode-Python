# https://leetcode.com/problems/ransom-note/
#Reference https://discuss.leetcode.com/topic/53889/many-different-ways-1-liners-2-liners-concise-4-liner-in-python-80ms/2
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# Subscribe to see which companies asked this question
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))