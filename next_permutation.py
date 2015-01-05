"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):  # pure math, more practice
        k = -1;
        #Step 1: find max k A[k]<A[k+1]
        for i in range(0,len(num)-1):
            if num[i]<num[i+1]:
                k = i;
        if k == -1:
            num.reverse();
            return num;
        else:
            #Step 2: find l A[l]>A[k]
            for i in range(k+1, len(num)):
                if num[i]>num[k]:
                    l = i;
            #Step 3: swap A[l] A[k]
            num[l], num[k] = num[k], num[l];
            #Step 4: reverse k+1 to end
            num[k+1:len(num):1] = num[len(num)-1:k:-1];
            return num;