"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True

        if len(s) == 1:
            return True

        alphanum = 'abcdefghijklmnopqrstuvwxyz1234567890'
        left = 0
        right = len(s) - 1

        while left <= right:
            c1 = s[left].lower()
            c2 = s[right].lower()
            if c1 not in alphanum:
                left += 1
                continue
            if c2 not in alphanum:
                right -= 1
                continue
            if c1 != c2:
                return False
            left += 1
            right -= 1

        return True
