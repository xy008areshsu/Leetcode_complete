#include <vector>
#include <map>
#include <unordered_map>
#include <iostream>

using namespace std;


  // Definition for undirected graph.
 struct UndirectedGraphNode {
      int label;
      vector<UndirectedGraphNode *> neighbors;
      UndirectedGraphNode(int x) : label(x) {};
 };
 


// struct KeyHasher
// {
//   std::size_t operator()(const Key& k) const
//   {
//     using std::size_t;
//     using std::hash;
//     using std::string;

//     return ((hash<string>()(k.first)
//              ^ (hash<string>()(k.second) << 1)) >> 1)
//              ^ (hash<int>()(k.third) << 1);
//   }
// };

class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == nullptr)
        	return nullptr;

        unordered_map<int, UndirectedGraphNode*> new_nodes;
        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> parent;

        parent[node] = nullptr;
        dfs(node, new_nodes, parent);

        for (auto item : parent) {
        	auto k = item.first;
        	for (auto n : k->neighbors) {
        		new_nodes[k->label]->neighbors.push_back(new_nodes[n->label]);
        	}
        }

        return new_nodes[node->label]; 
    }

    void dfs(UndirectedGraphNode* node, unordered_map<int, UndirectedGraphNode*>& new_nodes, unordered_map<UndirectedGraphNode*, UndirectedGraphNode*>& parent) {
    	new_nodes[node->label] = new UndirectedGraphNode(node->label);

    	for (auto n : node->neighbors) {
    		if (parent.find(n) == parent.end()) {
    			parent[n] = node;
    			dfs(n, new_nodes, parent);
    		}
    	}
    }
};

int main()
{
	Solution sol;

	return 0;
}