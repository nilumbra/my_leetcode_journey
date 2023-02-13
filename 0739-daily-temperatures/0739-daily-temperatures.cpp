class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
       stack<pair<int, int>> coldDays; // index, # of days accumulated
       
       int n = temperatures.size();
       vector<int> ans(n);
       for (int i = 0; i < n; i++) {
         int day_diff = 0;
        // pop until the top of coldDays stack is not colder current day (top >= current)
         while (coldDays.size() > 0 && (temperatures[coldDays.top().first] < temperatures[i])) {
           pair<int, int> colderDay = coldDays.top();
           coldDays.pop(); // found the first warmer day
           
           ans[colderDay.first] = colderDay.second + day_diff; // total # days passed until a warmer day
           day_diff += colderDay.second;
         }
         
         // cout << temperatures[i] << ',' << day_diff << endl;
         if (coldDays.size() > 0) {
           pair<int, int> warmerDay = coldDays.top();
           warmerDay.second += day_diff;
           // cout << temperatures[warmerDay.first] << ',' << warmerDay.second << endl;
           coldDays.pop();
           coldDays.push(warmerDay);
         }
         
         coldDays.push({i, 1}); // accumulated days initially = 1
         // cout << "========" << endl;
       }
      
      
       return ans;
    }
};