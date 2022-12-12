class Solution {
public:
    string removeDuplicateLetters(string S) {
        int count[26] = { 0 };
        int isInStack[26] = { 0 };


        // count the freq 
        for (char c: S) {
            count[c - 'a']++;
            // cout << c << ':' << count[c - 'a'] << endl;
            // cout << c;
        }

        // stack<char> T;
        string res;
        // add to stack 
        char c;
        for (char c: S) {
            count[c - 'a']--;
            // The stack maintains an invariant of increasing lexiographic order.
            // So if c is already in the stack, we shouldn't add it again, otherwise the invariant will be broken.
            if (isInStack[c - 'a']) {
              continue;
            }

            // while the stack is not empty and the current character is greater than the top character and the frequence of the top character is greater than 0
            // cout << c <<endl;
            
            while (!res.empty() && (res.back() > c) && (count[res.back() - 'a'] > 0)) {
              isInStack[res.back() - 'a'] = 0;
              res.pop_back();
            }
            // cout << "----" << endl;

            res.push_back(c);
            isInStack[c - 'a'] = 1;
            
            // cout << res << endl;
        }


            // char chrs[T.size() + 1]; 

            // chrs[T.size()] = '\0';

//             while (!T.empty()) {
//                 // cout << T.top();
//                 res.append(1, T.top());
//                 // chrs[T.size() - 1] = T.top();
//                 T.pop();
//             }

            // reverse(res.begin(), res.end());

        return res;
    }
};