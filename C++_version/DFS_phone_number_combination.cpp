class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        string str_aux;

        unordered_map<char, vector<string> > phone_map {
        	{'2', {"a", "b", "c"}},
        	{'3', {"d", "e", "f"}},
        	{'4', {"g", "h", "i"}},
        	{'5', {"j", "k", "l"}}, 
        	{'6', {"m", "n", "o"}},
        	{'7', {"p", "q", "r", "s"}},
        	{'8', {"t", "u", "v"}},
        	{'9', {"w", "x", "y", "z"}}
        };

        helper(digits, res, str_aux, phone_map, 0);

        return res;
    }

    void helper(string digits, vector<string>& res, string& str_aux, unordered_map<char, vector<string> >& phone_map, string::size_type pos) {
    	if (str_aux.length() == digits.length()) {
    		res.emplace_back(str_aux);
    		return;
    	}

    	for (string::size_type i = pos; i < digits.length(); ++i) {
    		for (auto s : phone_map[digits[i]]) {
    			str_aux += s;
    			helper(digits, res, str_aux, phone_map, i + 1);
    			str_aux = str_aux.substr(0, str_aux.length() - 1);
    		}
    	}
    }
};