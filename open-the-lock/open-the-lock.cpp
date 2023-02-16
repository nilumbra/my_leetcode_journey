// #include "bits/stdc++.h"
// using namespace std;
class Solution {
  public:
	vector<string> neighbor(string curr) {
      vector<string> neighbors;
      for (int i = 0; i < 4; i++) {
        // up 
        string up(4, ' ');
        copy(curr.begin(), curr.end(), up.begin());
	    up[i] = up[i] == '9' ? '0' : up[i] + 1;  
        neighbors.push_back(up);
        // down
        string down(4, ' ');
        copy(curr.begin(), curr.end(), down.begin());
        down[i] = down[i] == '0' ? '9' : down[i] - 1;
        neighbors.push_back(down);
      }
      
      return neighbors;
    }
  
    int openLock(vector<string>& deadends, string target) {
       
       queue<string> Q({"0000"}); 
       int steps = 0;
       set<string> visited(deadends.begin(), deadends.end());
       if (target == "0000") return 0;
       if (visited.count("0000") != 0) return -1; 
      
       // BFS
       while (!Q.empty()) {
          int lvSize = Q.size();
          for (int i = 0; i < lvSize; i++) {
            string curr = Q.front();
            Q.pop();
            
            for (string nei: neighbor(curr)) {
              if (nei == target)
                return steps + 1;
              if (visited.count(nei) == 0) {
                Q.push(nei);
                visited.insert(nei);
              }
            }            
          }
         
         steps++;
       }
      
      // BFS ends; entire connected graph traversed yet still no path found!
      return -1; 
    }
 
};

// int main(void) { 
//      S* s = new S();
//      vector<string> deadends {"0201","0101","0102","1212","2002"};
//      cout << s->openLock(deadends, "0202") << endl;
// //      vector<string> d;
// //      cout << s->openLock(d, "0009") << endl;
// //    for (auto& str: s->neighbor("0000"))
// //    cout << str << endl;
// //    cout << s->neighbor("0000") <<endl;
  
// 	return 0;
// }
  