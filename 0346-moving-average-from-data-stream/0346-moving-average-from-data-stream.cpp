// places got wrong
// 1. int / int = int, to get double from divisions btw. int, explicitly cast at least one of int to double
// 2. choice of initial value of `head` and `tail`
class MovingAverage {
  private:
    long arr[1000];
    int capacity;
    long long sum;
    
    int head;
    int tail;
  
    bool isFull() {
      return (tail + 1) % capacity == head;      
    }
  
    int size() {
      if (head <= tail) {
        //cout<< tail - head + 1 << endl; 
        return tail - head + 1;
      }
      else {
        //cout<< capacity - (head - tail) + 1 << endl; 
        return capacity - (head - tail) + 1;
      }
    }
    
  public:
    MovingAverage(int size) {
        capacity = size;
        sum = 0;
        head = 0;
        tail = -1;
    }
    
    double next(int val) { 
        if(tail != -1 && isFull()) {
          sum -= arr[head];
          head = (head + 1) % capacity; // deque
        }
        
        tail = (tail+1) % capacity;
        arr[tail] = val; // enque
        sum += val;
         
        return sum / (double) size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */