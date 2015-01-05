"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):   # more practice
        s = self.strip_words(s)
        s_list = self.split_words(s)
        s_list.reverse()
        s = ' '.join(s_list)
        s = self.strip_words(s)
        return s

    def strip_words(self, s):
        start = 0
        while start < len(s):
            if s[start] != ' ':
                break
            start += 1

        if start == len(s):
            return ''
        else:
            s = s[start : ]

        end = len(s) - 1
        while end >= 0:
            if s[end] != ' ':
                break
            end -= 1

        if end >= 0:
            s = s[: end + 1]

        return s

    def split_words(self, s):
        s = self.strip_words(s)
        if len(s) == 0:
            return []

        res = []
        i = 0
        j = 0

        while i < len(s):
            while j < len(s) and s[j] != ' ':  # find the end of a word
                j += 1
            res.append(s[i : j])

            while j < len(s) and s[j] == ' ':  # find the end of the middle spaces
                j += 1

            i = j

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.split_words('   I    am    a   hereo     '))
    print(sol.split_words('a'))


