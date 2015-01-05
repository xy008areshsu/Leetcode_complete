"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]

        res = []
        root = n * '0'
        parent = {root : None}
        self.helper(n, res, root, parent)

        return [self.b2d(b) for b in res]

    def helper(self, n, res, node, parent):
        res.append(node)

        for neighbor in self.neighbors(node):
            if neighbor not in parent:
                parent[neighbor] = node
                self.helper(n, res, neighbor,  parent)

    def neighbors(self, node):
        res = []

        for i in range(len(node)):
            if node[i] == '0':
                new_node = node[:i] + '1' + node[i+1:]
            else:
                new_node = node[:i] + '0' + node[i+1:]
            res.append(new_node)

        res.reverse()  # to deal with leetcode's limiation: For now, the judge is able to judge based on one
        # instance of gray code sequence. Sorry about that.
        return res

    def b2d(self, num):
        degree = len(num) - 1

        res = 0
        for i in range(len(num)):
            res += int(num[i]) * (2 ** degree)
            degree -= 1

        return res


