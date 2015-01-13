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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
  		auto i = 1;
  		auto dummy = new ListNode(0);
  		dummy->next = head;
  		auto cur = head;
  		auto prev = dummy;

  		while (i < m) {
  			if (cur == nullptr)
  				break;
  			++i;
  			cur = cur->next;
  			prev = prev->next;
  		}

  		if (cur == nullptr)
  			return nullptr;

  		auto start = cur;
  		auto prev_start = prev;
  		prev = start;
  		cur = cur->next;

  		while (i < n) {
  			if (cur == nullptr)
  				break;
  			auto temp = cur->next;
  			cur->next = prev;
  			prev = cur;
  			cur = temp;
  			++i;
  		}

  		if (i == n) {
  			start->next = cur;
  			prev_start->next = prev;
  			return dummy->next;
  		}

  		return nullptr;

    }
};

int main()
{
	Solution sol;

	return 0;

}