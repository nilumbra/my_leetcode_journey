#define INF 2147483647
//#define D4 {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        // iterate through the grid from top to bottom, left to right
        int m = rooms.size();
        int n = rooms[0].size();
        int D4[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
             // when find a gate, do BFS from that gate
             if (rooms[i][j] == 0) {
                queue<pair<int, int>> Q;
                set<pair<int, int>> visited;
                pair<int, int> gate(i, j); // define the gate as (int, int)
                Q.push(gate);
                int step = 0;
                while (!Q.empty()) {
                   int level_size = Q.size();
                   for (int _l = 0; _l < level_size; _l++) {
                     pair<int, int> point = Q.front(); // process next position
                     Q.pop();
                     
                     int _i = point.first;
                     int _j = point.second;
                     // cout << _i << ',' << _j << endl;
                     for (int _ = 0; _ < 4; _++) {
                       int dx = D4[_][0];
                       int dy = D4[_][1];
                       // if it is larger than step
                       // 1. update the room's value if 
                       int nx = _i + dx;
                       int ny = _j + dy;
                       if (visited.count(make_pair(nx, ny)) == 0 && 
                           (nx >= 0 && nx < m &&
                            ny >= 0 && ny < n) && 
                           step < rooms[nx][ny]) { // because min(step) = 0, which is >= 0(a gate) and >= -1(a wall), a gate or a wall won't pass the if test
                         //cout << _i + dx << ',' << ny << endl;
                          //if (nx == 3 && ny == 3){
                          //  cout << _i << ',' << _j << "==" << rooms[_i][_j]<< endl;
                          //  cout << "gate = " << gate.first << ',' << gate.second << endl;
                          //  cout << "step = " << step << endl;
                          //  cout << "level size = " << level_size << endl;
                          //} 
                            
                          rooms[nx][ny] = step + 1; 
                          Q.push({nx, ny}); 
                          visited.insert({nx, ny});
                       }
                     }                     
                   } 
                   step += 1;
                }
             }
          }
        }  
    }
};