class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector <int> memory;
        int r1 = 0;
        
        for (auto& s: tokens) {
          if (s.compare("+") == 0 || s.compare("-") == 0 || s.compare("*") == 0 || s.compare("/") == 0) {
            // conversion failed because the input wasn't a number
            int op2 = memory.back();memory.pop_back();
            int op1 = memory.back();memory.pop_back();
            int res;
            switch(s[0]) {
                case('+'):
                  res = op1 + op2;
                break;
                case('-'):
                  res = op1 - op2;
                break;
                case('*'):
                  res = op1 * op2;
                break;
                case('/'):
                  res = op1 / op2;
                break;
            }
            cout << res << endl;
            memory.push_back(res);
          }
          else {
            cout << stol(s) << endl;
            memory.push_back(stol(s));
          }
        }
      
        
        return memory.back();
    }
};