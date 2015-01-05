class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = (n + 1)*[-1]   # f[i] means how many distinct ways to climb to the ith floor
        if n == 1:
            return 1
        if n == 2:
            return 2

        f[1] = 1
        f[2] = 2

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]
