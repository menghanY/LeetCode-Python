# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Subscribe to see which companies asked this question
# https://discuss.leetcode.com/topic/69235/python-one-pass-with-a-stack
def isValid( s):
    stack = []
    for c in s:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        elif (c == ')' and (stack and stack[-1] == '(')) or (c == '}' and (stack and stack[-1] == '{')) or (
                c == ']' and (stack and stack[-1] == '[')):
            stack.pop()
        else:
            return False
    return stack == []
