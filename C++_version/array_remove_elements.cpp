/**
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
    	if (n == 0)
    		return n;

    	int left = 0;
    	int right = n - 1;
    	while (left <= right) {
    		if (A[left] == elem) {
    			int temp = A[left];
    			A[left] = A[right];
    			A[right] = temp;
    			--right;
    		} else {
    			++left;
    		}
    	}  
    	return left;
    }
};