class MyStack {
private:
  queue<int> q1;
  queue<int> q2;
public: 
    MyStack() {
        // Pop O(1)
        // Push O(n)
    }
    
    void push(int x) {
      q2.push(x);

      while(!q1.empty()) {
        int e = q1.front();
        q1.pop();
        q2.push(e);
      }
      
      swap(q1, q2);
    }
    
    int pop() {
      if (q1.empty()) 
        return -1;
      
      int e = q1.front();
      q1.pop();
      return e;
    }
    
    int top() {
      return q1.front();
    }
    
    bool empty() {
      return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */