/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        return helper(1, n + 1);
    }

    vector<TreeNode* > helper(int start, int end) {
    	vector<TreeNode* > res;
    	if (start >= end) {
    		res.push_back(nullptr);
    		return res;
    	}

    	if (start == end + 1) {
    		res.push_back(new TreeNode(start));
    		return res;
    	}

    	for (int i = start; i < end; ++i) {
    		vector<TreeNode* > left_res = helper(start, i);
    		vector<TreeNode* > right_res = helper(i + 1, end);
    		for (auto l_root: left_res) {
    			for (auto r_root: right_res) {
    				 TreeNode* root = new TreeNode(i);
    				 root->left = l_root;
    				 root->right = r_root;
    				 res.push_back(root);
    			}
    		}
    	}

    	return res;
    }


};