 // Definition for singly-linked list with a random pointer.
 struct RandomListNode {
      int label;
      RandomListNode *next, *random;
      RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 };
 
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == nullptr)
        	return nullptr;

        auto dummy = new RandomListNode(0);
        unordered_map<RandomListNode*, RandomListNode*> h_map;
        auto new_cur = dummy;
        auto cur = head;
        while (cur) {
        	new_cur->next = new RandomListNode(cur->label);
        	new_cur = new_cur->next;
        	h_map[cur] = new_cur;
        	cur = cur->next;
        }

        cur = head;
        new_cur = h_map[cur];
        while (cur) {
        	if (h_map.find(cur->random) != h_map.end()) {
        		new_cur->random = h_map[cur->random];
        	}
        	cur = cur->next;
        	new_cur = new_cur->next;
        }
        return dummy->next;
    }
};