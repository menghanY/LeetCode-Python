# https://leetcode.com/problems/decode-string/
# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
class Solution(object):
    def rle_decoding(self, strs):
        res_list, cnt_list, res_str, cnt, i = [], [], '', 0, 0
        while i < len(strs):
            if strs[i].isdigit():
                cnt=cnt*10+int(strs[i])
                i += 1
                continue
            else:
                j = i
                while j < len(strs) and not strs[j].isdigit():
                    j += 1
                res_list.append(strs[i:j])
                cnt_list.append(cnt)
                cnt = 0
                i = j
        for k in range(len(res_list)):
            res_str += res_list[k] * cnt_list[k]
        return res_str
#https://discuss.leetcode.com/topic/57212/python-rle-solution-for-encoding-problem/2
    def decodeString(self, strs):

        stck = []
        for i in range(len(strs)):
            if strs[i] == ']':
                tstr = []
                while stck and stck[-1] != '[':
                    tstr.insert(0,stck.pop())
                if stck:
                    # pop out the '['
                    stck.pop()
                    # add the number
                    while stck and stck[-1].isdigit():
                        tstr.insert(0,stck.pop())
                    # add to result
                    stck.append(self.rle_decoding(''.join(tstr)))
            else:
                stck.append(strs[i])
        return ''.join(stck) if stck else ''