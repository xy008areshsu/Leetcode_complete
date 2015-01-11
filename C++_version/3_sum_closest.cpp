/**
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/

#ifndef SUM_H
#define SUM_H

#include <algorithm>
#include <vector>
#include <limits>
#include <math>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        if(num.size() < 3)
        	return 0;

        sort(begin(num), end(num));

        int closest = 9999999;
        int res = 0;
        for(int i = 0; i < num.size() - 2; ++i) {
        	int left = i + 1;
        	int right = num.size() - 1;
        	while (left < right) {
        		int _sum = num[i] + num[left] + num[right];
        		if (_sum == target)
        			return target;
        		else {
        			if(abs(_sum - target) < closest) {
        				closest = abs(_sum - target);
        				res = _sum;
        			}
        			if(_sum > target) 
        				right--;
        			else
        				left++;
        		}

        	}

        }
        return res;
    }
};


#endif