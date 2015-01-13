class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
        vector<vector<int> > res;
        if (num.size() == 0)
        	return res;

        sort(begin(num), end(num));
        vector<int> list_aux;
        vector<bool> visited (num.size(), false);
        helper(num, res, list_aux, visited);

        return res;
    }

    void helper(vector<int>& num, vector<vector<int> >& res, vector<int>& list_aux, vector<bool>& visited) {
    	if (list_aux.size() == num.size()) {
    		res.emplace_back(list_aux);
    		return;
    	}

    	for (vector<int>::size_type i = 0; i < num.size(); ++i) {
    		if (visited[i] || (i != 0 && visited[i - 1] == false && num[i] == num[i - 1]))
    			continue;

    		visited[i] = true;
    		list_aux.emplace_back(num[i]);
    		helper(num, res, list_aux, visited);
    		list_aux.pop_back();
    		visited[i] = false;
    	}
    }
};