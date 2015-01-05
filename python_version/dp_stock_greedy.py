"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):  # more practice
        if len(prices) == 0 or len(prices) == 1:
            return 0

        min_val = float('inf')
        max_val = -float('inf')
        looking = 0    # looking is 0 meaning is looking for the min_val, 1 is looking for max_val
        total_profit = 0

        for i in range(len(prices)):
            if looking == 0:
                if prices[i] < min_val:
                    min_val = prices[i]
                else:
                    looking = 1
                    max_val = prices[i]
            else:
                if prices[i] >= max_val:
                    max_val = prices[i]

                else:
                    looking = 0

                    total_profit += (max_val - min_val)
                    min_val = prices[i]

        if looking == 1:  # if is looking for max val when reaching the last element, we need to update total profit
            total_profit += prices[-1] - min_val

        return total_profit

if __name__ == '__main__':
    sol = Solution()
    prices = [1,4, 2]
    print(sol.maxProfit(prices))