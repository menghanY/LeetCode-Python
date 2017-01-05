# Sort Characters By Frequency
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = {}
        lst_str = set(list(s))
        for i in lst_str:
            print(s.count(i, 0, len(s)))
            temp[i] = s.count(i, 0, len(s))
        result = ''
        for i in sorted(temp, key=temp.get, reverse=True):
            result += i*temp[i]
        return result
