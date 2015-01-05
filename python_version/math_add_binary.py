"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):  # more practice
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        c = 0
        res = ''

        while idx_a >= 0 and idx_b >= 0:
            aux_res = int(a[idx_a]) + int(b[idx_b]) + c
            if aux_res > 1:
                aux_res = aux_res - 2
                c = 1
            else:
                c = 0
            res = str(aux_res) + res
            idx_a -= 1
            idx_b -= 1

        while idx_a >= 0:
            aux_res = int(a[idx_a]) + c
            if aux_res > 1:
                aux_res = aux_res - 2
                c = 1
            else:
                c = 0
            res = str(aux_res) + res
            idx_a -= 1

        while idx_b >= 0:
            aux_res = int(b[idx_b]) + c
            if aux_res > 1:
                aux_res = aux_res - 2
                c = 1
            else:
                c = 0
            res = str(aux_res) + res
            idx_b -= 1

        if c == 1:
            res = str(c) + res

        return res
