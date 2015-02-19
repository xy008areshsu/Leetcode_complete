"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

# step 1: determine the sign of the number, check str[0] if it is a sign
# step 2: loop, put each char into a list, until non numerical char is found
# step 3: calculate the value


class Solution:
    # @return an integer
    def atoi(self, str):   # more practice
        new_str = str.strip()
        if new_str == '':
            return 0

        if new_str[0] != '+' and new_str[0] != '-' and new_str[0] not in '1234567890':
            return 0

        if new_str[0] == '-' or new_str[0] == '+':
            sign = new_str[0]
            new_str = new_str[1:]
        else:
            sign = '+'

        i = 0
        int_list = []
        while i < len(new_str):
            if new_str[i] not in '1234567890':
                break
            int_list.append(new_str[i])
            i += 1

        if len(int_list) > 0:
            degree = len(int_list) - 1
            res = 0
            for d in int_list:
                res += int(d) * (10 ** degree)
                degree -= 1

            if sign == '-':
                res = -res
                if res < -2147483648:
                    res = -2147483648
            else:
                if res > 2147483647:
                    res = 2147483647
            return res


        return 0



if __name__ == '__main__':
    sol = Solution()
    print(sol.atoi('+1'))