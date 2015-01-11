class Solution {
public:
    int search(int A[], int n, int target) {
        if (n == 0)
        	return -1;

        if (n == 1)
        	if (A[0] == target)
        		return 0;
        	else
        		return -1;

       	int start = 0;
       	int end = n - 1;
       	while(start <= end) {
       		int mid = start + (end - start) / 2;
       		if (A[mid] == target)
       			return mid;
       		else {
       			if (A[mid] >= A[start])
       				if (target >= A[start] && target <= A[mid])
       					end = mid - 1;
       				else
       					start = mid + 1;
       			else
       				if (target >= A[mid] && target <= A[end])
       					start = mid + 1;
       				else
       					end = mid - 1;
       		}
       	}

       	return -1;
    }
};