#https://leetcode.com/problems/valid-parentheses/

#include <stack>
class Solution {
public:
    bool isValid(string s) {
        stack <char> st;
	for (auto a : s) {
		if (a == '(' || a == '[' || a == '{')
			st.push(a);
		if (a == ')' || a == ']' || a == '}') {
			if (st.empty()) {
				return false;
			}

			if (st.top() == a - 1 || st.top() == a - 2)
				st.pop();
			else {
				return false;
			}
		}
	}
	if (st.empty())
		return true;
	else
		return false;
    }
};
