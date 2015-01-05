"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):  # more practice
        if len(s) > 12:
            return []

        res = []
        list_aux = []
        self.helper(s, res, list_aux)

        return res

    def helper(self, s, res, list_aux):
        if len(list_aux) == 4 and s == '':
            res.append('.'.join(list_aux[:]))
            return

        for i in range(0, len(s)):
            prefix = s[: i + 1]
            if int(prefix) > 255:
                break
            if len(prefix) == 1 or (prefix[0] != '0'):
                list_aux.append(prefix)
                self.helper(s[i+1:], res, list_aux)
                list_aux.pop()