/**
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
*/

#include <vector>
#include <string>
#include <iostream>
#include <tuple>
#include <unordered_map>
#include <map>

using namespace std;

class pairhash {
public:
  template <typename T, typename U>
  std::size_t operator()(const std::pair<T, U> &x) const
  {
    return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
  }
};

class Solution {
public:
    bool exist(vector<vector<char> > &board, string word) {
        if (word.length() == 0)
        	return false;

        if (board.size() == 0)
        	return false;

        vector< vector<int> > head_idx;
        for (int i = 0; i < board.size(); ++i) {
        	for (int j = 0; j < board[i].size(); ++j) {
        		if (board[i][j] == word[0])
        			head_idx.push_back({i, j});
        	}
        }

        if (head_idx.size() == 0)
        	return false;

        for (auto idx: head_idx) {
        	string str_aux = word.substr(0, 1);
        	unordered_map<pair<int, int>, vector<int>, pairhash> parent;
        	pair<int, int> n_idx {idx[0], idx[1]};
        	parent[n_idx] = {};
        	if (helper(board, word, idx, str_aux, parent))
        		return true;
        }

        return false;
    }

    bool helper(vector<vector<char> >& board, string word, vector<int>& idx, string& str_aux, unordered_map<pair<int, int>, vector<int>, pairhash>& parent ) {
    	if (str_aux == word)
    		return true;

    	for (auto neighbor: neighbors(idx, board)) {
    		pair<int, int> n_idx {neighbor[0], neighbor[1]};
    		auto f = parent.find(n_idx);
    		if (parent.find(n_idx) == parent.end()) {
    			if (board[neighbor[0]][neighbor[1]] == word[str_aux.length()]) {
    				parent[n_idx] = idx;
    				str_aux += board[neighbor[0]][neighbor[1]];
    				if (helper(board, word, neighbor, str_aux, parent))
    					return true;
    				parent.erase(n_idx);
    				str_aux = str_aux.substr(0, str_aux.length() - 1);
    			}
    		}
    	}

    	return false;
    }

    vector<vector<int> > neighbors(vector<int>& node_idx, vector<vector<char> >& board) {
    	vector<vector<int> > res;
    	if (node_idx[0] - 1 >= 0)
    		res.push_back({node_idx[0] - 1, node_idx[1]});

    	if (node_idx[0] + 1 < board.size())
    		res.push_back({node_idx[0] + 1, node_idx[1]});

    	if (node_idx[1] - 1 >= 0)
    		res.push_back({node_idx[0], node_idx[1] - 1});

    	if (node_idx[1] + 1 < board[0].size())
    		res.push_back({node_idx[0], node_idx[1] + 1});

    	return res;
    }
};

int main()
{

	Solution sol;
	vector<vector<char> > board {
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'}
	};

	string word {"ABCB"};

	bool _exist = sol.exist(board, word);

	// unordered_map<pair<int, int>, vector<int> , pairhash> h;
	// h[make_pair<int, int>(1, 2)] = {3, 4};
	// pair<int, int> idx {1, 2};
	// auto val = h.find(idx);

	// if (val != h.end())
	// 	cout << h[idx][0] << endl;

	cout << _exist << endl;

	return 0;

}