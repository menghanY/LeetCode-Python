# https://leetcode.com/problems/bulb-switcher/
# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.


class Solution(object):
    def bulbSwitch(self, n):
        i = 1
        while i ** 2 <= n:
            i += 1
        return i - 1