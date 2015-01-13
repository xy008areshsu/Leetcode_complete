#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<string> version1_list = split(version1, ".");
        vector<string> version2_list = split(version2, ".");

        vector<string>::size_type length = min(version1_list.size(), version2_list.size());
        for (int i = 0; i < length; ++i) {
        	if (stoi(version1_list[i]) > stoi(version2_list[i]))
        		return 1;
        	else if (stoi(version1_list[i]) < stoi(version2_list[i]))
        		return -1;
        	else
        		continue;
        }

        if (version1_list.size() > version2_list.size()){
        	if (all_of(version1_list.begin() + version2_list.size(), version1_list.end(), [](string& s) {return stoi(s) == 0;}))
        		return 0;
        	return 1;
        }
        else if (version1_list.size() < version2_list.size()) {
        	if (all_of(version2_list.begin() + version1_list.size(), version2_list.end(), [](string& s) {return stoi(s) == 0;})) {
        		cout << stoi(*(version2_list.begin() + version1_list.size())) << endl;
        		return 0;
        	}
        	cout << stoi(*(version2_list.begin() + version1_list.size())) << endl;
        	return -1;
        }
        else
        	return 0;

    }


	vector<string> split(const string & str, const string & delimiters) {
	    vector<string> v;
	    string::size_type start = 0;
	    auto pos = str.find_first_of(delimiters, start);
	    while(pos != string::npos) {
	        if(pos != start) // ignore empty tokens
	            v.emplace_back(str, start, pos - start);
	        start = pos + 1;
	        pos = str.find_first_of(delimiters, start);
	    }
	    if(start < str.length()) // ignore trailing delimiter
	        v.emplace_back(str, start, str.length() - start); // add what's left of the string
	    return v;
	}
};

int main()
{
	Solution sol;
	string version1 = "1";
	string version2 = "1.0";
	int res = sol.compareVersion(version1, version2);

	cout << res << endl;

	return 0;
}