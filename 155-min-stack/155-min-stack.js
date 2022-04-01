
var MinStack = function() {
    this.minstack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if (this.minstack.length == 0 || val < this.getMin()) {
        this.minstack.push([val, val]) // [0] frame value, [1]: min value up to this frame
    } else {
        this.minstack.push([val, this.getMin()])
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.minstack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.minstack.at(-1)[0]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minstack.at(-1)[1]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */