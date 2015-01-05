class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1

        if len(needle) == 0 and len(haystack) == 0:
            return 0

        if len(needle) == 0 and len(haystack) != 0:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(needle) > len(haystack) - i:
                    return -1
                else:
                    if haystack[i : i + len(needle)] == needle:
                        return i

        return -1