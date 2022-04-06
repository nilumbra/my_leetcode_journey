/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    /*
     use two pointer to delineate the boundary of a consecutive body of trapped rain

     e.g. 
     [1,2,3,4,3,2,3]
    */

    //  left: at 0, currently known highest and rightmost position on the downhill side
    //  bottom: == left, lowest and rightmost position in a valley; left <= bottom <= right always holds
    //  right: left <= right, always increasing
    var vol = 0;
    var [peaks, non_increasing] = findPeaks(height), left;
         

    console.log(peaks, non_increasing)
    if(non_increasing){
        console.log("reversing")
        let l = height.length;
        peaks = peaks.map(i => l-i-1).reverse();
        height = height.reverse();
    }

    left = peaks[0];
    for(const [idx, peak_idx] of peaks.slice(1).entries()) {
        /** loop invariant: left is the heightest in peaks[left, idx] after an execution of trappedRain()
        */

        if(idx == peaks.length - 2 || height[left] <= height[peak_idx] || height[peak_idx] >= height[peaks[idx+2]]){ // if left peak smaller than or equal to current peak, calc trapped rain
            console.log(idx == peaks.length - 2, height[left] <= height[peak_idx], [peak_idx] >= height[peaks[idx+2]])
            console.log(`trappedRain(${left}, ${peak_idx})`)
            vol += trappedRain(height, left, peak_idx)
            console.log(left, peak_idx, vol)
            left = peak_idx
        }
    } 

    //calculate the trap if there is one
                // if(isTrapFormed()) {
                // //calculate trap
                // vol += trappedRain(left, bottom, idx)
                // console.log("Trap formed: ", `left:${left}`, `bottom${left}`, `idx:${idx}`, `vol:${vol}`)

            // }

    
    /** Find and return all peaks in height
     *  @return {number}
     */
    function findPeaks(height){
        var peaks = [],
             left = 0,
       decreasing = true;

        for (const [idx, el] of height.entries()) {
            if (idx == 0 && height[idx] > height[idx + 1] || height[idx - 1] <= height[idx] && height[idx + 1] < height[idx] || !height[idx + 1]  && height[idx] > height[idx - 1]){
                peaks.push(idx);
                decreasing = !peaks.at(-2) || decreasing && height[peaks.at(-2)] >= height[peaks.at(-1)];
                // console.log(decreasing, height[peaks.at(-2)], height[peaks.at(-1)]);
            }
        }
        return [peaks, decreasing]
    }
    
    /** Calculate trapped rain vol given a trap configuration
     * @param {number} left
     * @param {number} right
     * @erturn {number} 
     */
    function trappedRain(height, left, right){
        while(height[left + 1] >= height[right] || height[right - 1] >= height[left]){
            // console.log(left, right);
            if (height[left] == height[right]){
                break
            }

            if (height[left] > height[right]) {
                left++;
            } else {
                right--;
            }
        }

        const level = Math.min(height[left], height[right]),
               rect = left >= right ? 0 : level * (right - left - 1),
           nonwater = left + 1 >= right? 0 : height.slice(left + 1, right).reduce((acc,curr) => acc+curr);
        console.log(`left:${left}`, `right:${right}`,`level: ${level}, rect:${rect}, nonwater:${nonwater}`);
        return rect - nonwater
    }

    return vol    
};