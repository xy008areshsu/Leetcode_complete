/**
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
*/


 // Definition for binary tree
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void flatten(TreeNode *root) {
        if (root == nullptr)
        	return;

        if (root->left == nullptr && root->right == nullptr)
        	return;

       	//if (root->left) 
       		flatten(root->left);
       	//if (root->right)
       		flatten(root->right);

       	if (root->left == nullptr)
       		return;

       	TreeNode *cur = root->left;
       	while (cur->right)
       		cur = cur->right;

       	cur->right = root->right;
       	root->right = root->left;
       	//delete root->left;
       	root->left = nullptr;
    }
};             

int main()
{
	Solution sol;
	TreeNode *root = new TreeNode(1);
	root->left = new TreeNode(2);
	sol.flatten(root);

	return 0;

}