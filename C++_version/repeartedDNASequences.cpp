/**
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
*/

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> h_map;
        vector<string> res;

        if (s.length() < 10) {
            return res;
        }

        for (auto i = 0; i < s.length() - 9; ++i) {
            auto s_aux = s.substr(i, 10);
            auto it = h_map.find(s_aux);
            if (it == h_map.end()) {
                h_map[s_aux] = 1;
            } else {
                if (h_map[s_aux] == 1) {
                    res.push_back(s_aux);
                }
                h_map[s_aux] += 1;
            }
        }

        return res;
    }
};

int main()
{
    string s {""};
    Solution sol;
    auto res = sol.findRepeatedDnaSequences(s);
    cout << res.size() << endl;

    return 0;

}