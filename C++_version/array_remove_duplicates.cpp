/**
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
*/

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n == 0 || n == 1)
        	return n;

        int first = 0;
        int second = 1;
        while (second < n) {
        	while(second < n && A[second] == A[first])
        		++second;

        	if (second < n) {
        		int temp = A[first + 1];
        		A[first + 1] = A[second];
        		A[second] = temp;
        		++first;
        		++second;
        	}
        }
        return (first + 1);

    }
};