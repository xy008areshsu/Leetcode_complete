
#include <iostream>

using namespace std;

 // Definition for singly-linked list.
  struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr)
        	return nullptr;

        auto lenA = 0;
        auto lenB = 0;
        auto cur = headA;
        while (cur){
        	lenA++;
        	cur = cur->next;
        }

        cur = headB;
        while (cur) {
        	lenB++;
        	cur = cur->next;
        }

        auto curA = headA;
        auto curB = headB;

        if (lenA > lenB) {
        	auto n = lenA - lenB;
        	auto i = 0;

        	while (i < n) {
        		if (curA == nullptr)
        			return nullptr;
        		++i;
        		curA = curA->next;
        	}
        } else {
        	auto n = lenB - lenA;
        	auto i = 0;
        	while (i < n) {
        		if (curB == nullptr)
        			return nullptr;
        		++i;
        		curB = curB->next;
        	}
        }

        while (curA && curB) {
        	if (curA == curB)
        		return curA;
        	curA = curA->next;
        	curB = curB->next;        	
        }

        return nullptr;

    }
};

int main()
{
	Solution sol;

	ListNode* headA = new ListNode(3);
	ListNode* headB = new ListNode(2);
	headB->next = new ListNode(3);
	ListNode* intersect = sol.getIntersectionNode(headA, headB);



	return 0;
}