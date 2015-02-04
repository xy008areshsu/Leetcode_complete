"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

# use h_map, record each element when scanning, key is the char, value is the index
# if each time, s[j] not in h_map, add it into h_map
# else, update result length first, then delete all of the element key in h_map with the index before s[j]


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):  # more practice
        length = 0
        if len(s) == 0:
            return 0

        h_map = {}
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in h_map:
                h_map[s[j]] = j
                j += 1
            else:
                if j - i > length:
                    length = j - i

                for k in range(i, h_map[s[j]]):  # the elements before s[j] is useless, cannot be counted, so need to be deleted from map
                    del(h_map[s[k]])

                i = h_map[s[j]] + 1
                h_map[s[j]] = j
                j += 1

        if j - i > length:
            length = j - i

        return length





if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar"))