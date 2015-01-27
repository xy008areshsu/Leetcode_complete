class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.size() == 0) {
        	return "";
        }

        if (strs.size() == 1) {
        	return strs[0];
        }

        auto res = strs[0];
        for(vector<string>::size_type i = 1; i < strs.size(); ++i) {
        	if (strs[i] == "") {
        		return "";
        	}

        	res = res.substr(0, min(res.length(), strs[i].length()));

        	for(auto j = 0; j < res.length(); ++j) {
        		if (res[j] != strs[i][j]) {
        			res = res.substr(0, j);
        		}
        	}
        }
        return res;
    }
};