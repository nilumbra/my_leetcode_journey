
var MinStack = function() {
    this.stack = [];
    this.minheap = new MinHeap()

};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if (this.stack.length == 0 || val <= this.getMin()) {
        this.minheap.insert(val)
    }
    this.stack.push(val) 
};


/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (this.stack[0] < this.getMin()){ console.error("Untracked min detected!! Stack data is corrupted.")}
    if (this.stack[this.stack.length - 1] == this.getMin()) {
        this.minheap.extractMin()
    }

    this.stack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack.at(-1)
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minheap.data[0]
};


function MinHeap() {
  this.data = [];
}

MinHeap.prototype.insert = function(val) {
  this.data.push(val);
  this.bubbleUp(this.data.length-1);
};

MinHeap.prototype.bubbleUp = function(index) {
  while (index > 0) {
    // get the parent
    var parent = Math.floor((index + 1) / 2) - 1;
    
    // if parent is greater than child
    if (this.data[parent] > this.data[index]) {
      // swap
      var temp = this.data[parent];
      this.data[parent] = this.data[index];
      this.data[index] = temp;
    }
    
    index = parent;
  }
};

MinHeap.prototype.extractMin = function() {
  var min = this.data[0];
  
  // set first element to last element
  this.data[0] = this.data.pop();
  
  // call bubble down
  this.bubbleDown(0);
  
  return min;
};

MinHeap.prototype.bubbleDown = function(index) {
  while (true) {
    var child = (index+1)*2;
    var sibling = child - 1;
    var toSwap = null;
    
    // if current is greater than child
    if (this.data[index] > this.data[child]) {
      toSwap = child;
    }
    
    // if sibling is smaller than child, but also smaller than current
    if (this.data[index] > this.data[sibling] && (this.data[child] == null || (this.data[child] !== null && this.data[sibling] < this.data[child]))) {
        toSwap = sibling;
    }
    
    // if we don't need to swap, then break.
    if (toSwap == null) {
      break;
    }
    
    var temp = this.data[toSwap];
    this.data[toSwap] = this.data[index];
    this.data[index] = temp;
    
    index = toSwap;
  }
};

module.exports = MinStack
/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */