#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        if (s.length() > 12)
        	return res;

        vector<string> list_aux;

        helper(s, res, list_aux);

        return res;
    }

    void helper(string s, vector<string>& res, vector<string>& list_aux) {
    	if (list_aux.size() == 4 && s == "") {
    		//copy(begin(list_aux), end(list_aux), std::ostream_iterator<string>(oss, "."));
    		//string a {oss.str()};
    		string a = accumulate(begin(list_aux), end(list_aux), string{""}, [](string partial_res, string p) {return partial_res + p + ".";});
    		a = a.substr(0, a.length() - 1);
    		res.emplace_back(a);
    		return;
    	}

    	for (string::size_type i = 0; i < s.length(); ++i) {
    		string prefix = s.substr(0, i + 1);
    		if (stoi(prefix) > 255)
    			break;
    		if (prefix.length() == 1 || prefix[0] != '0') {
    			list_aux.emplace_back(prefix);
    			helper(s.substr(i+1), res, list_aux);
    			list_aux.pop_back();
    		}
    	}
    }
};


int main()
{
	Solution sol;
	string s {"0000"};
	vector<string> res = sol.restoreIpAddresses(s);

	for (auto s: res)
		cout << s << endl;

	return 0;
}