class MyCircularQueue {
private:
    int capacity;
    int length;
    int head;
    int tail;
    int Q [1000];
public:
    void printQ() {
      for(int i = 0;i < length; i++) {
        cout << Q[i % capacity]<< " ";
      }
      cout << endl;
    }
    MyCircularQueue(int k) {
       capacity = k; 
       length = 0;
       head = 0;
       tail = -1; 
    }
    
    bool enQueue(int value) {
       if(isFull()) return false;
       length++;
       tail = (head + length - 1) % capacity;
       Q[tail] = value;
       //cout << length << endl;
      return true;
    }
    
    bool deQueue() {
       if (isEmpty()) return false;
       head = (head + 1) % capacity;
       length--;
       
       return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return Q[head];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return Q[tail];
    }
    
    bool isEmpty() {
        return length == 0;
    }
    
    bool isFull() {
        return length == capacity;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */