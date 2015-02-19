/**
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
*/


//  Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
    	vector<vector<int> > res;
		if (root == nullptr) {
			return res;
		}

		vector<int> list_aux;
		helper(root, sum, res, list_aux);

		return res;
    }

    void helper(TreeNode* root, int sum, vector<vector<int> >& res, vector<int>& list_aux) {
    	if (root->left == nullptr && root->right == nullptr) {
    		if (root->val == sum) {
    			list_aux.push_back(root->val);
    			res.push_back(list_aux);
    			list_aux.pop_back();    			
    		}
    		return;
    	}

    	list_aux.push_back(root->val);
    	if (root->left)
    		helper(root->left, sum - root->val, res, list_aux);
    	if (root->right)
    		helper(root->right, sum - root->val, res, list_aux);
    	list_aux.pop_back();
    }

};