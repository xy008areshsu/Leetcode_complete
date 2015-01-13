#include <vector>
#include <string>
#include <iostream>
#include <tuple>
#include <map>

using namespace std;


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
        	map<vector<int>, vector<int> > parent { {idx, {}}};
        	if (helper(board, word, idx, str_aux, parent))
        		return true;
        }

        return false;
    }

    bool helper(vector<vector<char> >& board, string word, vector<int>& idx, string& str_aux, map<vector<int>, vector<int> >& parent ) {
    	if (str_aux == word)
    		return true;

    	for (auto neighbor: neighbors(idx, board)) {
    		if (parent.find(neighbor) == parent.end()) {
    			if (board[neighbor[0]][neighbor[1]] == word[str_aux.length()]) {
    				parent[neighbor] = idx;
    				str_aux += board[neighbor[0]][neighbor[1]];
    				if (helper(board, word, neighbor, str_aux, parent))
    					return true;
    				parent.erase(neighbor);
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

	cout << _exist << endl;

	return 0;

}