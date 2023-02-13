class MinStack {
  vector<pair<int, int>> data; // val, min
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (data.size() == 0) 
          data.push_back({val, val}); // min is just val
        else {
          pair<int, int> top = data.back();
          int new_min = min(top.second, val);
          data.push_back({val, new_min});
        }
    }
    
    void pop() {
        if (data.size() > 0) 
          data.pop_back();
    }
    
    int top() {
        return data.back().first;
    }
    
    int getMin() {
       return data.back().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */