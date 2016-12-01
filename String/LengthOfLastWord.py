# https://leetcode.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
class Solution(object):
    def lengthOfLastWord(self, s):
        while len(s) and s[-1] == ' ':
            s = s[0:-1]
        wordLength = 0
        for i in s[::-1] :
            if i == ' ' : break
            wordLength += 1
        return wordLength
s = Solution()
print(s.lengthOfLastWord(" "))
