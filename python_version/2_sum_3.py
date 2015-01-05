"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.h_map = {}

    # @return nothing
    def add(self, number):
        if number in self.h_map:
            self.h_map[number] += 1
        else:
            self.h_map[number] = 1


    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for k in self.h_map.keys():
            if value - k in self.h_map:
                if value - k != k:   # must consider the case of value = 6, k = 3; if h_map[3] > 1 then it is True
                    return True
                elif self.h_map[value - k] > 1:
                    return True

        return False
