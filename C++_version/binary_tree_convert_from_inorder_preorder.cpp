#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

//Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        if (inorder.size() != preorder.size())
        	return nullptr;

        if (inorder.size() == 0)
        	return nullptr;

        return helper(inorder, 0, inorder.size() - 1, preorder, 0, preorder.size() - 1);

    }


    TreeNode *helper(vector<int> &inorder, int in_begin, int in_end, vector<int> &preorder, int pre_begin, int pre_end) {

    	TreeNode *root = new TreeNode(preorder[pre_begin]);

        int root_idx_inorder {-1};
        for (int i = in_begin; i <= in_end; ++i) {
        	if (inorder[i] == root->val) {
        		root_idx_inorder = i;
        		break;
        	}
        } 
        if (root_idx_inorder == -1)
        	return nullptr;


        TreeNode *left_root = helper(inorder, in_begin, root_idx_inorder - 1, preorder, pre_begin + 1, pre_begin + (root_idx_inorder - 1 - in_begin) + 1);
        TreeNode *right_root = helper(inorder, root_idx_inorder + 1, in_end, preorder, pre_begin + (root_idx_inorder - 1 - in_begin) + 2, pre_end);

        root->left = left_root;
        root->right = right_root;

        return root;       
    }
};

int main()
{
	Solution sol;
	vector<int> preorder {1, 2};
	vector<int> inorder {2, 1};
	TreeNode *root = sol.buildTree(preorder, inorder);

	cout << root->val << endl;



	return 0;

}