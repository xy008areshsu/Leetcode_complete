"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.


T is "ece" which its length is 3.
"""

#idea : maintain a h_map, keys are each char, and vals are lists of indices of each char, each val is a sorted list, since the index goes from 0 to len(s) - 1
# scan the string, if the char already in h_map, append the index of that char to the value list.
# else, if len(h_map) still less than 2, add this char into the h_map
# else, find the minimum index and remove it from the value list. If any value list is empty, then delete the corresponding key. Repeat this until the length of
# h_map is less than 2.
# update the longest length at each step of the for loop

import collections

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):  # More practice,
        if s is None:
            return 0
        if len(s) == 0 or len(s) == 1 or len(s) == 2:
            return len(s)

        h_map = {}
        longest_len = 0
        for i, c in enumerate(s):
            if c in h_map:
                h_map[c].append(i)
            else:
                if len(h_map) < 2:
                    h_map[c] = collections.deque()
                    h_map[c].append(i)
                else:
                    while len(h_map) >= 2:
                        c_min, indices = min(h_map.items(), key = lambda x:x[1][0])  # list of index are sorted lists

                        h_map[c_min].popleft()
                        if len(h_map[c_min]) == 0:
                            del h_map[c_min]

                    h_map[c] = collections.deque()
                    h_map[c].append(i)
            c_min, i_min = min(h_map.items(), key = lambda x : x[1][0])
            c_max, i_max = max(h_map.items(), key = lambda x : x[1][-1])
            i_min = i_min[0]
            i_max = i_max[-1]
            if i_max - i_min + 1 > longest_len:
                longest_len = i_max - i_min + 1


        c_min, i_min = min(h_map.items(), key = lambda x : x[1][0])
        c_max, i_max = max(h_map.items(), key = lambda x : x[1][-1])
        i_min = i_min[0]
        i_max = i_max[-1]
        if i_max - i_min + 1> longest_len:
            longest_len = i_max - i_min + 1


        return longest_len





if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct('cdaba'))
    print(sol.lengthOfLongestSubstringTwoDistinct('ccaabbb'))
    print(sol.lengthOfLongestSubstringTwoDistinct('abadc'))
    print(sol.lengthOfLongestSubstringTwoDistinct('aac'))
    print(sol.lengthOfLongestSubstringTwoDistinct('abacd'))



