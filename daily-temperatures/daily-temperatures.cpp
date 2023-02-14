class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
       vector<pair<int, int>> coldDays; // index, # of days accumulated
       
       int n = temperatures.size();
       vector<int> ans(n);
       for (int i = 0; i < n; i++) {
         int curr_temp = temperatures[i];
         
         while (coldDays.size() > 0 && temperatures[coldDays.back().first] < curr_temp) {
           pair<int, int> coldDay = coldDays.back();
           int dayIndex = coldDay.first;
           int daySince = coldDay.second;
           coldDays.pop_back();
           
           if (coldDays.size() > 0) {
             // pair<int, int> last = coldDays.back();
             coldDays.back().second += daySince;
           }
           
           ans[dayIndex] = daySince;
         }
         
         coldDays.push_back({i ,1});
       }
       
      
       return ans;
    }
};