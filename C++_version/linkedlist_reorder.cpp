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
    void reorderList(ListNode *head) {
        if (head == nullptr || head->next == nullptr)
        	return;

        ListNode* mid = find_mid(head);
        ListNode* left = head;
        ListNode* right = mid->next;
        mid->next = nullptr;
        right = reverse(right);
        left = merge(left, right);

        head = left;
    }

    ListNode* find_mid(ListNode* head) {
    	if (head == nullptr || head->next == nullptr || head->next->next == nullptr)
    		return head;

    	ListNode* slow = head;
    	ListNode* fast = head->next;
    	while (fast && fast->next) {
    		slow  = slow->next;
    		fast = fast->next->next;
    	}

    	return slow;
    }

    ListNode* reverse(ListNode* head) {
    	if (head == nullptr || head->next == nullptr)
    		return head;

    	ListNode* prev = nullptr;
    	ListNode* cur = head;
    	while (cur) {
    		ListNode* temp = cur->next;
    		cur->next = prev;
    		prev = cur;
    		cur = temp;
    	}

    	head = prev;
    	return head;
    }

    ListNode* merge(ListNode* left, ListNode* right) {
    	if (left == nullptr)
    		return right;

    	if (right == nullptr)
    		return left;

    	auto dummy = new ListNode(0);
    	auto cur = dummy;
    	auto cur_left = left;
    	auto cur_right = right;
    	int count = 0;
    	while (cur_left && cur_right) {
    		if (count == 0) {
    			cur->next = cur_left;
    			cur_left = cur_left->next;
    			count = 1;
    		} else {
    			cur->next = cur_right;
    			cur_right = cur_right->next;
    			count = 0;
    		}
    		cur = cur->next;
    	}

    	if (cur_left) {
    		cur->next = cur_left;
    	}

    	if (cur_right) {
    		cur->next = cur_right;
    	}

    	return dummy->next;

    }
};