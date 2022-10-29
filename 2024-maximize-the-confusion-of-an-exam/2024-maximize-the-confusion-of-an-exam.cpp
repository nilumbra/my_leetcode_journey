class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        //string A = "TF";
        int maximum = 0;
        for (auto c: "TF") {
          queue<int> Q;
          int s = 0, i = 0, mian = k;
          for (;i < answerKey.length();i++) {
            if (answerKey[i] == c) {
               continue;
            } else if (answerKey[i] != c && mian == 0) {
              int fi = Q.front();
              Q.pop();
              maximum = max(maximum, i - s);
              //cout << i << ":" << maximum << endl;
              s = fi + 1;
              Q.push(i); 
              
              //mian += 1;
            } else {
              Q.push(i);
              mian--;
            }
          }         
          maximum = max(maximum, i - s);
          //cout << i << ":" << maximum << endl;
          //cout << "\n";
        }

        return maximum;
    }
};