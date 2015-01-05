# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        new_nodes = {}
        parent = {node : None}
        self.dfs(node, new_nodes, parent)

        for k in parent.keys():
            for n in k.neighbors:
                new_nodes[k.label].neighbors.append(new_nodes[n.label])

        return new_nodes[node.label]

    def dfs(self, node, new_nodes, parent):
        new_nodes[node.label] = UndirectedGraphNode(node.label)

        for n in node.neighbors:
            if n not in parent:
                parent[n] = node
                self.dfs(n, new_nodes, parent)