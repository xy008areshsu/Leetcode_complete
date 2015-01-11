class Solution {
public:
    int findMin(vector<int> &num) {
        if (num.size() == 0)
        	return 0;
        if (num.size() == 1)
        	return num[0];
        if (num.size() == 2)
        	return min(num[0], num[1]);

        int pivot = -1;
        int start = 0;
        int end = num.size() - 1;

        while (start + 1 < end) {
        	int mid = start + (end - start) / 2;
        	if (num[mid] < num[mid - 1] && num[mid] < num[mid + 1]) {
        		pivot = mid;
        		break;
        	} else if (num[mid] < num[start]) {
        		end = mid;
        	} else {
        		start = mid;
        	}
        }

        if (pivot == -1) {
        	if (num[start] > num[end])
        		pivot = end;        	
        }

        if (pivot == -1)
        	pivot = 0;

        return num[pivot];
    }
};