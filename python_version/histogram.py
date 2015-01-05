"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""


class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):   # More practice
        s = []
        largest_area = 0
        for i in range(len(height) + 1):
            if i != len(height):
                h = height[i]
            else:
                h = -1   # important!, to ensure all elements will be popped out of the stack finally

            while len(s) > 0 and h < height[s[-1]]:
                h_top = height[s.pop()]
                if len(s) == 0:
                    w = i
                else:
                    w = i - s[-1] - 1
                largest_area = max(largest_area, h_top * w)
            s.append(i)

        return largest_area




if __name__ == '__main__':
    height = [2,0,2]
    sol = Solution()
    print(sol.largestRectangleArea(height))

