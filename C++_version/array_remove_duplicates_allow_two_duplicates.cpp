/**
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
*/

#include <iostream>

using namespace std;

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n == 0 || n == 1 || n == 2)
        	return n;

        int first = 0;
        int second = 0;
        if(A[0] == A[1]) {
        	first = 1;
        	second = 2;
        } else {
        	first = 0;
        	second = 1;
        }

        while (second < n) {
        	while (second < n && A[first] == A[second]) 
        		++second;
    		
    		if (second < n) {
    			int temp = A[first + 1];
    			A[first + 1] = A[second];
    			A[second] = temp;
    			++first;
    			++second;

    			if (second < n && A[first] == A[second]) {
    				int temp = A[first + 1];
    				A[first + 1] = A[second];
    				A[second] = temp;
    				++first;
    				++second;
    			}
    		}   	
        }
        return (first + 1);
    }
};

int main()
{
	Solution sol;
	int A[3] = {1, 2, 3}; 
	int res = sol.removeDuplicates(A, 3);
	cout << res << endl;

	return 0;
}