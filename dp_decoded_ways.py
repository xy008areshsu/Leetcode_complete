"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

# function:  f[i] = number of ways to decode for first i + 1 elements of S
# update: 1. consider if S[i] == 0, then check if S[i-1: i+1] is a valid encoded number, if so, then f[i] = f[i -2], else, return 0, there is no way to encode
#         2. if S[i] != 0, then check if S[i-1: i+1] is a valid encoded number, if so, then f[i] = f[i - 1] + f[i - 2], because S[i] must be a valid encoded number if it is not 0
#                                                                                  else: f[i] = f[i - 1]
# init: f[0] = 1 if S[0] != '0' else return 0
#       if s[1] == 0: if s[0:2] in map: f[1] = 1, else return 0
#       else if s[1] != 0: if s[0 : 2] in map: f[1] = 2, else f[1] = 1
# final solution: f[len(S) - 1]

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):   # This one should consider many test cases: '0', '', '01', '10', '150', '120', '121'   more practice
        map = {d:c for d in ['1', '2', '3','4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'
        ,'18', '19', '20', '21', '22', '23', '24', '25', '26'] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

        if len(s) == 0:
            return 0

        if len(s) == 1:
            if s[0] in map:
                return 1
            else:
                return 0

        f = len(s) * [0]
        if s[0] == '0':
            return 0
        else:
            f[0] = 1  # initialization
            if s[1] == '0':
                if s[0:2] in map:
                    f[1] = 1
                else:
                    return 0
            else:
                if s[0:2] in map:
                    f[1] = 2
                else:
                    f[1] = 1

            for i in range(2, len(s)):
                if s[i] == '0':
                    if s[i - 1: i + 1] in map:
                        f[i] = f[i - 2]
                    else:
                        return 0
                else:
                    if s[i - 1: i + 1] in map:
                        f[i] = f[i - 2] + f[i - 1]
                    else:
                        f[i] = f[i - 1]

        return f[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('100'))
