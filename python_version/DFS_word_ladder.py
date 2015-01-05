"""
Word Ladder 1
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

"""

import time

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):   # more practice
        parent_forward = {start : None}
        parent_backward = {end : None}
        frontier_forward = [start]
        frontier_backward = [end]
        level_forward = {start : 1}
        level_backward = {end : 1}
        i = 2
        j = 2

        while frontier_forward and frontier_backward:
            next_forward = []
            for node in frontier_forward:
                for neighbor in self.get_neighbors(node, dict):
                    if neighbor not in parent_forward:
                        parent_forward[neighbor] = node
                        next_forward.append(neighbor)
                        level_forward[neighbor] = i
                        if neighbor == end:
                            return level_forward[neighbor]
                        if neighbor in parent_backward:
                            return level_forward[neighbor] + level_backward[neighbor] - 1
            i += 1
            frontier_forward = next_forward

            next_backward = []
            for node in frontier_backward:
                for neighbor in self.get_neighbors(node, dict):
                    if neighbor not in parent_backward:
                        parent_backward[neighbor] = node
                        level_backward[neighbor] = j
                        next_backward.append(neighbor)
                        if neighbor == start:
                            return level_backward[neighbor]
                        if neighbor in parent_forward:
                            return level_backward[neighbor] + level_forward[neighbor] - 1
            j += 1
            frontier_backward = next_backward

        if end in level_forward:
            return level_forward[end]
        if start in level_backward:
            return level_backward[start]

        return 0

    def get_neighbors(self, node, dict):
        neighbors = []
        for i in range(len(node)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != node[i]:
                    new_node = node[:i] + c + node[i+1:]
                    if new_node in dict:
                        neighbors.append(new_node)

        return neighbors



