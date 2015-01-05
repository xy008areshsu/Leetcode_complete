"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

# idea:
# two functions: best_left[i] best profit scanning from left rto right;  best_right[i] best profit scanning from right to left.  Same as stock_1 to update the two functions
# combine: best_right reverse, then for i in range(len(best_left) - 1) find an i  that maximizes best_left[i] + best_right[i]


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):   # more practice
        if len(prices) == 0 or len(prices) == 1:
            return 0

        best_left = [0]
        best_right = [0]

        #first scan from left to right
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > best_left[-1]:
                best_left.append(prices[i] - min_price)
            else:
                best_left.append(best_left[-1])


        max_price = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]

            if max_price - prices[i] > best_right[-1]:
                best_right.append(max_price - prices[i])
            else:
                best_right.append(best_right[-1])

        max_profit = 0
        best_right.reverse()
        for i in range(len(best_left) - 1):
            max_profit = max(max_profit, best_left[i] + best_right[i + 1])  # these are for exactly two transactions

        max_profit = max(max_profit, best_left[-1])  # this is for just one transaction

        return max_profit

if __name__ == '__main__':
    prices = [3,2,6,5,0,3]
    sol = Solution()
    print(sol.maxProfit(prices))