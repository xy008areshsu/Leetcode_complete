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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if (head == nullptr)
        	return nullptr;

        auto i = 1;
        auto fast = head;
        while (i != n) {
        	if (fast == nullptr)
        		return nullptr;
        	++i;
        	fast = fast->next;
        }

        auto slow = head;
        auto dummy = new ListNode(0);
        dummy->next = head;
        auto prev = dummy;
        while (fast->next) {
        	fast = fast->next;
        	slow = slow->next;
        	prev = prev->next;
        }

        prev->next = slow->next;

        return dummy->next;
    }
};