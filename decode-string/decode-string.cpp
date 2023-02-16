class Solution {
public:
    // assume s[-1] is a number
    int atoi(stack<char>& s) {
      int k = 0;
      int base = 1;
      // cout << s.top();
      while (!s.empty() && isdigit(s.top())) 
      {
        k += (s.top()-'0') * base;
        base *= 10;
        s.pop();
      }
      return k; 
    }

    // resize `s` to k * s.size()
    // copy the seq of characters in s by k times
    void multiply(vector<char>& s, int k) {
      int originalSize = s.size();
      s.resize(originalSize * k);
      for (int i = 1; i < k; i++) 
          copy(s.begin(), s.begin() + originalSize, s.begin() + i * originalSize);
    } 
  
    string decodeString(string s) {
      // use two stack
      stack<char> parse;
      for(char c: s) 
      {
        if (c == ']') 
        {
          string decodedString = "";
          char top = parse.top();
          while (top != '[') { // find a k[encoded_string] pattern, "backtrack" to pase
              decodedString += top;
              parse.pop();
              top = parse.top();
          }
          parse.pop(); // now top == '[', pop it, then the chars before that become `k`
          
          int k = atoi(parse);

          while (k != 0) 
          {
            for (int j = decodedString.size() - 1; j >= 0; j--) 
            {
              parse.push(decodedString[j]);  
            }
            k--;
          }
        } else 
        {
          parse.push(c);
        }
      }
      
      
      string res;
      while (!parse.empty())
      {
        res += parse.top();
        parse.pop();
      }
      reverse(res.begin(), res.end());
      // reverse_copy(build.begin(), build.end(), res.begin());
      // cout << res << endl;
      return res;
    }
};