/**
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
*/

#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        vector<vector<int> > res;
        if (num.size() < 3)
            return res;

        sort(begin(num), end(num));

        for (int i = 0; i < num.size() - 2; ++i) {
            if(i != 0 && num[i] == num[i - 1])
                continue;
            int left = i + 1;
            int right = num.size() - 1;
            while(left < right){
                if(num[i] + num[left] + num[right] == 0) {
                    vector<int> res_aux = {num[i], num[left], num[right]};
                    res.push_back(res_aux);
                    ++left;
                    --right;
                    while(left < right && num[left] == num[left - 1])
                        ++left;

                    while(left < right && num[right] == num[right + 1])
                        --right;
                }
                else if(num[i] + num[left] + num[right] < 0) {
                    ++left;
                }
                else
                    --right;
            }
        }

        return res;
    }
};