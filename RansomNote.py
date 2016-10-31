#Reference https://discuss.leetcode.com/topic/53889/many-different-ways-1-liners-2-liners-concise-4-liner-in-python-80ms/2
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))