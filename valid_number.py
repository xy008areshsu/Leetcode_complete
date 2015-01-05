"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self,s):  # more practice
        s = s.strip()     # remove all of the white spaces
        if len(s) == 0:
            return False

        s_list = list(s)
        if s_list[0] not in '+-1234567890.':    # consider only the first place
            return False
        if s_list[-1] == 'e':           # consider the last place
            return False

        if s[:2] == '.e':
            return False

        count_e = 0
        count_point = 0
        if s_list[0] in '+-':          # + and - can only be placed in the head,  '.' can be placed anywhere
            s_list = s_list[1:]

        if s_list[0] == '.':
            s_list = s_list[1:]
            count_point = 1

        if len(s_list) == 0:
            return False

        for i in range(len(s_list)):
            if s_list[i] not in '1234567890.e':
                return False
            if s_list[i] == 'e':
                count_e += 1
                if count_e > 1 or (i != len(s_list) - 1 and s_list[i + 1] == '.'):
                    return False
            if s_list[i] == '.':
                count_point += 1
                if count_point > 1:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isNumber('.e1'))