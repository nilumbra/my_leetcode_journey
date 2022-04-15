/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    const stack = [],
          nxt_gr = new Map();
    for (const num of nums2) {
        if (stack.at(-1) < num) {
            while (stack.at(-1) < num) {
                nxt_gr.set(stack.pop(), num)
            }
        }
        stack.push(num)
    }
    // console.log(nxt_gr)

    return nums1.map(num=>nxt_gr.get(num)||-1)
};