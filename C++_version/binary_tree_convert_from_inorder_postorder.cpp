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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        if (inorder.size() != postorder.size())
        	return nullptr;

        if (inorder.size() == 0)
        	return nullptr;

        return helper(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);

    }


    TreeNode *helper(vector<int> &inorder, int in_begin, int in_end, vector<int> &postorder, int post_begin, int post_end) {

    	TreeNode *root = new TreeNode(postorder[post_end]);

        int root_idx_inorder {-1};
        for (int i = in_begin; i <= in_end; ++i) {
        	if (inorder[i] == root->val) {
        		root_idx_inorder = i;
        		break;
        	}
        } 
        if (root_idx_inorder == -1)
        	return nullptr;


        TreeNode *left_root = helper(inorder, in_begin, root_idx_inorder - 1, postorder, post_begin, post_begin + (root_idx_inorder - 1 - in_begin));
        TreeNode *right_root = helper(inorder, root_idx_inorder + 1, in_end, postorder, post_begin + (root_idx_inorder - 1 - in_begin) + 1, post_end - 1);

        root->left = left_root;
        root->right = right_root;

        return root;       
    }
};

int main()
{
	Solution sol;
	vector<int> inorder {1, 3, 2};
	vector<int> postorder {3, 2, 1};
	TreeNode *root = sol.buildTree(inorder, postorder);

	cout << root->right->left->val << endl;



	return 0;

}