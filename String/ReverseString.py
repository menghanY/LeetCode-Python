class Solution(object):
    def reverseString(self, s):
        strList = list(s)
        strList.reverse()
        return "".join(strList)