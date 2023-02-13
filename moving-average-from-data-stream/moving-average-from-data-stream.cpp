// places got wrong
// 1. int / int = int, to get double from divisions btw. int, explicitly cast at least one of int to double
// 2. choice of initial value of `head` and `tail`
class MovingAverage {
  private:
    queue<int> Q;
    long long sum;
    int capacity;
  public:
    MovingAverage(int size) {
       sum = 0;
       capacity = size;
    }
    
    double next(int val) { 
      if (Q.size() == capacity) {
        int front = Q.front();
        Q.pop();
        sum -= front;
      } 
      sum += val;
      Q.push(val);
      return sum / (double) Q.size();
   }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */