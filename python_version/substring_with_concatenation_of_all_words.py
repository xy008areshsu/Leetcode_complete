"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

"""


"""
Analysis:

Try to think this problem straightforward:
Say in L there are m strings with length n.
What string is required to match in S?     A length of m*n string start with each position in S.
What is a match?  In the m*n long string, every string in L appear only once.

So the algorithm is:
Scan every m*n long string start from each position in S, see if all the strings in L have been appeared only once using Map data structure. If so, store the starting position.

Yes, do not consider any DP or DFS solutions, just using the hash map and loop.
"""


import time
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integerS
    def findSubstring(self, S, L):   # more practice
        start_time = time.time()
        h_map = {}
        if len(L) == 0:
            return S == ''

        for str_l in L:
            if str_l not in h_map:
                h_map[str_l] = 1
            else:
                h_map[str_l] += 1

        res = []
        i = 0
        m = len(L[0])
        n = len(S)
        while i + len(L) * m - 1 < len(S):  # if look ahead, len(L) * m will over pass the last element of S, there is no need to keep doing it, the remaining of S is too short
            h_map_2 = {}
            j = 0
            while j < len(L):
                subs = S[i + j * m : i + (j + 1) * m]
                if subs not in h_map:
                    break
                else:
                    if subs not in h_map_2:
                        h_map_2[subs] = 1
                    else:
                        h_map_2[subs] += 1
                    if h_map_2[subs] > h_map[subs]:
                        break
                    j += 1
            if j == len(L):
                res.append(i)
            i += 1
        print("my method: " + str(time.time() - start_time))
        return res


    def yu_method(self, S, L):
        start_time = time.time()
        res = []            # result list
        num = len(L)        # length of the str list
        ls = len(S)
        if num == 0:
            return []
        str_len = len(L[0]) # length of each str
        #create the map: count the occurrance of each string
        #Note that set(L) is used to reduce the time, otherwise will not pass the large test
        map_str = dict((x,L.count(x)) for x in set(L))
        i = 0
        while i + num * str_len - 1 < ls:
            map_str2 = {}
            j = 0
            while j < num:
                subs = S[i + j * str_len:i + j * str_len + str_len ]
                if not subs in map_str:
                    break
                else:
                    # Note that dict.get(key, default_val) is used to handel the case that key NOT exist
                    map_str2[subs] = map_str2.get(subs, 0) + 1
                    if map_str2[subs]>map_str[subs]:
                        break
                    j = j + 1
            if j == num:
                res.append(i)
            i = i + 1
        print('Yu method: ' + str(time.time() - start_time))
        return res




if __name__ == '__main__':
    sol = Solution()
    S = 'barfoothefoobarman'
    L = ["bar", "foo"]
    print(sol.yu_method(S, L))
    print(sol.findSubstring(S, L))