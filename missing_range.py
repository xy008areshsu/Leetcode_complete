"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""

class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        res = []
        if len(A) == 0:
            if upper > lower:
                return [str(lower) + '->' + str(upper)]
            elif upper == lower:
                return [str(upper)]
            else:
                raise Exception('Wrong')


        i = 0
        while i < len(A):
            if A[i] < lower:
                i += 1
                continue
            else:
                break

        if A[i] - 1 > lower:
            res.append(str(lower) + '->' + str(A[i] - 1))
        elif A[i] - 1 == lower:
            res.append(str(lower))

        i += 1

        while i < len(A):
            if A[i] <= upper:
                if A[i] - 2 == A[i - 1]:
                    res.append(str(A[i - 1] + 1))
                elif A[i] - 2 > A[i - 1]:
                    res.append(str(A[i - 1] + 1) + '->' + str(A[i] - 1))
                i += 1
            else:
                break

        if upper - 1 > A[i - 1]:
            res.append(str(A[i - 1] + 1) + '->' + str(upper))
        elif upper - 1 == A[i - 1]:
            res.append(str(upper))

        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.findMissingRanges([0, 1], 0 , 1))

