/**
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
*/

#include <string>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <climits>

using namespace std;

class Solution {
public:
    int atoi(const char *str) {
        string s{str};
        s.erase(s.begin(), std::find_if(s.begin(), s.end(), std::bind1st(std::not_equal_to<char>(), ' ')));  // remove leading spaces,  
        // remove trailing spaces: value.erase(std::find_if(value.rbegin(), value.rend(), std::bind1st(std::not_equal_to<char>(), ' ')).base(), value.end());
        if(s.length() == 0)
        	return 0;

        string::iterator it;
        string numeric {"1234567890"};
        it = find(begin(numeric), end(numeric), s[0]);

        if(s[0] != '+' && s[0] != '-' && it == end(numeric))
        	return 0;

        char sign;
        if(s[0] == '+' || s[0] == '-') {
			sign = s[0];
			s = s.substr(1);
        } else
        	sign = '+';

        int i = 0;
        vector<int> int_list;
        while (i < s.length()) {
        	it = find(begin(numeric), end(numeric), s[i]);
        	if (it == end(numeric))
        		break;
        	int d = stoi(s.substr(i, 1));   // use stoi(const string&) here instead of atoi, since atoi will take  a const char* as its argument,
        	int_list.push_back(d);
        	++i;
        }

        if (int_list.size() > 0) {
        	bool plus_one = false;
        	auto degree = int_list.size() - 1;
        	int res {0};
        	for(auto d: int_list) {
        		if (d * (pow(10, degree)) >= INT_MAX - res) {  
        		    if (sign == '-' && (d* (pow(10, degree)) >= INT_MAX - res + 1))
        				plus_one = true;      			
        			res = INT_MAX;
        			break;
        		}
        		res += d * (pow(10, degree));
        		--degree;
        	}

        	if (sign == '-')  {
        		res = -res;
        		if (plus_one)
        			res -= 1;
        	}

        	return res;
        }

        return 0;
    }
};


int main()
{
	Solution sol;
	int j = sol.atoi("-2147483649");
	cout << j << endl;


	return 0;
}