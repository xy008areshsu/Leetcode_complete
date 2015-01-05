"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        st = []

        for c in s:
            if c in ')]}' and len(st) == 0:
                return False
            if c in '([{':
                st.append(c)
            if c == ')':
                if st.pop() != '(':
                    return False
            if c == ']':
                if st.pop() != '[':
                    return False
            if c == '}':
                if st.pop() != '{':
                    return False

        if len(st) == 0:
            return True

        return False
