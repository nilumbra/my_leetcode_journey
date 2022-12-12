class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk({-1});
        int mx = 0;
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);
                } else {
                    mx = max(mx, i - stk.top());
                }
            }
        }

        return mx;
    }
};