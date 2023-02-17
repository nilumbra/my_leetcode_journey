#include <iostream>
#include <deque>
using namespace std;

class Solution {
public:
  /*
   * Canonical path CFG: 
   * CP -> ROOT DIR
   * DIR -> dirName (/dirname)*
   *
   * dirname = [a-zA-z]+
   * ROOT = \/
   */
  
  string simplifyPath(string path) {
    deque<string> parse;
    // Read in one token  
    string TOKEN;
    int readDIR = 0; // flag to mark the state: reading dirname
    for (int i = 1; i < (int)path.size(); i++) {
      char c = path[i];
      
      if (c == '/') {
        if (readDIR) {
          if (TOKEN == ".."){
            if(!parse.empty()) parse.pop_back(); // back up to parent dir
          }
          else if (TOKEN == ".")
			      TOKEN.clear();            
          else 
            parse.push_back(TOKEN);
          
          TOKEN.clear();
          readDIR = 0;  
        } 
        // it's an extra /, ignore
      }
      else {
        readDIR = readDIR | 1;
        TOKEN += c;
      }
    }
	
    //cout << "Last token: " << TOKEN << endl;
    if (TOKEN == ".." ){
      if(!parse.empty()) parse.pop_back(); // back up to parent dir
    }
    else if (TOKEN != "." && TOKEN.size() > 0)
      parse.push_back(TOKEN);
	
    // cout << "token queue size: " << parse.size() << endl;
    string res = "/"; // root
    while(!parse.empty()) {
      //cout << parse.front() << " --> " << endl;
      res += parse.front() + '/';
      parse.pop_front();
    }

    if (res.length() > 1) {
      // cout << "in string simplify: " << res << endl;
      res.pop_back();
    }
    return res;
  }
};