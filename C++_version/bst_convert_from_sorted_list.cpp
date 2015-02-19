#include <vector>
#include <iostream>

using namespace std;

// Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
 

  // Definition for binary tree
  struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
 

class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        if (head == nullptr)
        	return nullptr;

        if (head->next == nullptr) {
        	TreeNode *root = new TreeNode(head->val);
        	return root;
        }

        if (head->next->next == nullptr) {
        	TreeNode *root = new TreeNode(head->next->val);
        	root->left = new TreeNode(head->val);
        	return root;
        }

        vector<ListNode* > middles = find_mid(head);
        ListNode* prev_mid = middles[0];
        ListNode* mid = middles[1];
        prev_mid->next = nullptr;
        TreeNode* left_root = sortedListToBST(head);
        TreeNode* right_root = sortedListToBST(mid->next);
        TreeNode* root = new TreeNode(mid->val);
        root->left = left_root;
        root->right = right_root;

        return root;

    }

    vector<ListNode* > find_mid(ListNode* head) {
    	vector<ListNode* > res {nullptr, nullptr};
    	if (head == nullptr)
    		return res;

    	if (head->next == nullptr) {
    		res[1] = head;
    		return res;
    	}

    	if (head->next->next == nullptr) {
    		res[0] = head;
    		res[1] = head->next;
    		return res;
    	}

    	if (head->next->next->next == nullptr) {
    		res[0] = head;
    		res[1] = head->next;
    		return res;
    	}

    	ListNode* slow = head;
    	ListNode* fast = head->next;

    	while (fast && fast->next) {
    		if (fast->next->next == nullptr) 
    			res[0] = slow;
    		else if (fast->next->next->next == nullptr)
    			res[0] = slow;

    		slow = slow->next;
    		fast = fast->next->next;
    	}

    	res[1] = slow;
    	return res;

    }

};


int main()
{
	Solution sol;
	ListNode* head = new ListNode(-10);
	head->next = new ListNode(-3);
	head->next->next = new ListNode(0);
	head->next->next->next = new ListNode(5);
	head->next->next->next->next = new ListNode(9);
	TreeNode* root = sol.sortedListToBST(head);

	return 0;

}