"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

# idea:
# use a T_map and a counter to maintain

class Solution:
    # @return a string
    def minWindow(self, S, T):   # More practice
        if len(S) < len(T):
            return ''

        T_map = {}
        for item in T:
            if item not in T_map:
                T_map[item] = 1
            else:
                T_map[item] += 1


        start = 0
        end = 0
        window = ''
        size = float('inf')
        count = 0
        while end < len(S):
            if S[end] in T_map:
                if T_map[S[end]] > 0:
                    count += 1
                T_map[S[end]] -= 1     # T_map[S[end]] should decrement anyway

            while count == len(T):
                new_size = end - start + 1
                if new_size < size:
                    size = new_size
                    window = S[start : end + 1]

                if S[start] in T_map:
                    T_map[S[start]] += 1    # T_map[S[start]] should increment anyway
                    if T_map[S[start]] > 0:
                        count -= 1

                start += 1

            end += 1

        return window