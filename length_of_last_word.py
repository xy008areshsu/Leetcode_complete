"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):   # More practice
        if len(s) == 0:
            return 0

        s = s.split()
        if len(s) > 0:
            return len(s[-1])
        return 0

    def method2(self, s):
        count = 0
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == ' ':
                if count == 0:
                    continue
                else:
                    return count
            count += 1

        return count


