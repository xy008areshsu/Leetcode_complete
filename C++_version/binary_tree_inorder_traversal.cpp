/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <algorithm>
#include <vector>

class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
    	vector<int> res;
        if (root == nullptr)
        	return res;

        vector<int> left_res = inorderTraversal(root->left);
        copy(left_res.begin(), left_res.end(), back_inserter(res));
        //res.insert(res.end(), left_res.begin(), left_res.end());   // Both are correct
        res.push_back(root->val);
        vector<int> right_res = inorderTraversal(root->right);
        copy(right_res.begin(), right_res.end(), back_inserter(res));
        //res.insert(res.end(), right_res.begin(), right_res.end());   // Both are correct

        return res;
    }

    vector<int> inorderTraversal_iter(TreeNode *root) {

    	vector<TreeNode*> st;

    	vector<int> res;

    	if (root == nullptr)
    		return res;

    	TreeNode *cur = root;

    	while (cur) {
    		st.push_back(cur);
    		cur = cur->left;
    	}

    	while (st.size() > 0) {
    		TreeNode *node = st.back();
    		st.pop_back();
    		res.push_back(node->val);
    		node = node->right;
    		while (node) {
    			st.push_back(node);
    			node = node->left;
    		}
    	}

    	return res;

    }
};