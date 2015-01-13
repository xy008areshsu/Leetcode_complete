/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        if (head == nullptr)
        	return nullptr;

        auto left_dummy = new ListNode(0);
        auto right_dummy = new ListNode(0);
        auto left = left_dummy;
        auto right = right_dummy;

        auto cur = head;

        while (cur) {
        	if (cur->val >= x) {
        		right->next = new ListNode(cur->val);
        		right = right->next;
        	} else {
        		left->next = new ListNode(cur->val);
        		left = left->next;
        	}
        	cur = cur->next;
        }

        left->next = right_dummy->next;
        return left_dummy->next;
    }
};