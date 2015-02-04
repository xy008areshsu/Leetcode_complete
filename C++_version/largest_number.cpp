#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(string a, string b) {
	if (a + b > b + a) {
		return true;
	} else {
		return false;
	}
}

class Solution {
public:
    string largestNumber(vector<int> &num) {
    	vector<string> num_str;
    	for (auto n : num) {
    		num_str.push_back(to_string(n));
    	}

        sort(begin(num_str), end(num_str), compare);

        string res;

        bool leading_zero = true;
        for(auto n : num_str) {
        	if (leading_zero) {
        		if (n != "0") {
        			leading_zero = false;
        			res += n;
        		} else {
        			continue;
        		}
        	} else {
        		res += n;
        	}
        }

        if (res == "") {
        	res = "0";
        }

        return res;
    }
};



int main()
{
	Solution sol;
	vector<int> num {3, 30, 34, 5, 9};
	string res = sol.largestNumber(num);
	cout << res << endl;

	return 0;
}