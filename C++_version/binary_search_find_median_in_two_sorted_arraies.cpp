/**
"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
*/

#include <iostream>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if ((m + n) % 2 == 0)
        	return (find_kth(A, m, B, n, (m + n) / 2) + find_kth(A, m, B, n, (m + n) / 2 + 1)) / 2.0;
        else
        	return (find_kth(A, m, B, n, (m + n) / 2 + 1));
    }

    double find_kth(int A[], int m, int B[], int n, int k) {
    	if (m <= 0)
    		return B[k - 1];
    	if (n <= 0)
    		return A[k - 1];
    	if (k <= 1)
    		return min(A[0], B[0]);
    	if (m / 2 + n / 2 + 1 >= k) {
    		if (B[n/2] >= A[m/2])
    			return find_kth(A, m, B, n / 2, k);
    		else
    			return find_kth(A, m / 2, B, n, k);
    	} else {
    		if (B[n/2] >= A[m/2])
    			return (A + m/2, m/2, B, n, k - m/2 + 1);
    		else
    			return (A, m, B + n/2, n/2, k - n/2  + 1);
    	}
    }
};

int main()
{
	Solution sol;
	int A[2] = {1,2};
	int B[1] = {3};
	cout << sol.findMedianSortedArrays(A, 2, B, 1) << endl;
}