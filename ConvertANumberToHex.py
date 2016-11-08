#reference https://discuss.leetcode.com/topic/66358/python-35-ms-solution-95th
class Solution(object):
    def toHex(self, num):
        if num == 0: return '0'
        map = '0123456789abcdef'
        ret = ''

        # 32 bit == 4 byte each x char represents 4 bits, half a byte
        for i in range(8):  # at max we have 32 bit integer, so 8 iterations of computing 4 bits in each iteration == 32 bits
            cur = num & 0b1111  # get least significant 4 bits, this corresponds to least significant hex char
            char = map[cur]  # fetch hex char
            ret = char + ret  # append hex char to return
            num = num >> 4  # erase the 4 bits we just computed for next iteration
        pos = 0
        while pos < len(ret) and ret[pos] == '0':
            pos += 1
        return ret[pos:]
