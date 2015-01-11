/**
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
*/

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

//  Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumNumbers(TreeNode *root) {
    	if (root == nullptr) {
    		return 0;
       	}

       	vector<string> res;
       	string str_aux;
       	helper(root, res, str_aux);

       	int res_sum = accumulate(begin(res), end(res), 0, [](int partial_res, string s) {return partial_res + stoi(s);});
       	return res_sum;
    }

    void helper(TreeNode* root, vector<string>& res, string& str_aux) {
    	if (root->left == nullptr && root->right == nullptr) {
    		res.push_back(str_aux + to_string(root->val));
    		return;
    	}

    	str_aux += to_string(root->val);
    	if (root->left)
    		helper(root->left, res, str_aux);
    	if (root->right)
    		helper(root->right, res, str_aux);
    	str_aux = str_aux.substr(0, str_aux.length() - 1);
    }
};


int main()
{

	Solution sol;
	TreeNode* root = new TreeNode(4);
	root->left = new TreeNode(9);
	root->right = new TreeNode(0);
	root->left->right = new TreeNode(1);
	int res = sol.sumNumbers(root);
	cout << res << endl;

	return 0;

}