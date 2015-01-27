class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() == 1) {
        	return s;
        }

        string res = "";

        for (auto i = 0; i < s.length() - 1; ++i) {
        	auto palindrom1 = expand(s, i, i);
        	auto palindrom2 = expand(s, i, i + 1);
        	if (palindrom1.length() > res.length()) {
        		res = palindrom1;
        	}
        	if (palindrom2.length() > res.length()) {
        		res = palindrom2;
        	}
        }

        return res;
    }

    string expand(const string& s, int c1, int c2) {
    	auto left = c1;
    	auto right = c2;

    	while (left >= 0 && right < s.length()) {
    		if (s[left] == s[right]) {
    			left--;
    			right++;
    		} else {
    			break;
    		}
    	}

    	return s.substr(left + 1, right - left - 1);
    }
};