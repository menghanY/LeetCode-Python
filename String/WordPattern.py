# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

class Solution(object):
    def wordPattern(self, pattern, str):
        strList = str.split(" ")
        strListLen = len(strList)
        if len(pattern) != strListLen: return False
        patternStr = {}
        for index in range(strListLen):
            value = patternStr.get(pattern[index],0)
            if value == 0 :
                if strList[index] not in patternStr.values():
                    patternStr[pattern[index]] = strList[index]
                else:
                    return False
            else:
                if patternStr[pattern[index]] != strList[index] :
                    return False
        return True

s = Solution()
print(s.wordPattern("abba","dog cat cat fish"))

