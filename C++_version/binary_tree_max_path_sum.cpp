#include <climits>

using namespace std;

//  Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 

struct Result
{
	int single_path_sum;
	int max_path_sum;
};

class Solution {
public:
    int maxPathSum(TreeNode *root) {
		Result res = helper(root);
		return res.max_path_sum;	        
    }

    Result helper(TreeNode *root) {
    	Result res;
    	if (root == nullptr) {
    		res.single_path_sum = 0;
    		res.max_path_sum = INT_MIN;
    		return res;
    	}

    	Result left_res = helper(root->left);
    	Result right_res = helper(root->right);
    	res.single_path_sum = max(max(left_res.single_path_sum, right_res.single_path_sum) + root->val, root->val);
    	res.max_path_sum = max(left_res.max_path_sum, right_res.max_path_sum);
    	res.max_path_sum = max(max(max(res.max_path_sum, res.single_path_sum), left_res.single_path_sum + right_res.single_path_sum + root->val), root->val);

    	return res;
    }
};