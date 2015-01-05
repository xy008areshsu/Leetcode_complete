"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Hide Tags
"""

# idea:
# see source code

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        minimum = prices[0]
        max_profit = 0
        for p in prices:
            if p - minimum > max_profit:
                max_profit = p - minimum
            if p < minimum:
                minimum = p
        return max_profit