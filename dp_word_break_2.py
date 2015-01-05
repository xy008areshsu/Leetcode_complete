"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):  # more practice
        if s is None:
            return []

        if len(s) == 0:
            return []

        if len(s) == 1:
            if s in dict:
                return [s]
            else:
                return []

        memo = {}
        return self.helper(s, dict, memo)

    def helper(self, s, dict, memo):
        if s in memo:
            return memo[s]

        res = []

        for i in range(len(s)):
            if s[:i+1] in dict:
                if i == len(s) - 1:
                    res.append(s[:i+1])
                else:
                    rest = self.helper(s[i+1:], dict, memo)
                    for item in rest:
                        res.append(s[:i+1] + ' ' + item)

        memo[s] = res
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print(sol.wordBreak(s, dict))


