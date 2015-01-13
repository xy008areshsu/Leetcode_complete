class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        string titles = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        while (n > 0) {
        	int rem = n % 26;
        	n /= 26;
        	if (rem == 0) {
        		rem = 26;
        		n -= 1;
        	}
        	res = titles[rem] + res;
        }

        return res;
    }
};