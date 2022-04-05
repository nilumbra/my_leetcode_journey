/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function(num) {
    const num_word_conversion = {
        1: "One",
        2: "Two",
        3: "Three", 
        4: "Four",
        5: "Five",
        6: "Six", 
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
    }
    
    
    // Input: Only expects an int in range 0 <= int <= 999
    // Output: English word representation for int
    function three_digit_conversion(int){
        if (int === 0) return ""
        
        var word = "";
        // Get hundredth place
        if(int >= 100){
            word += num_word_conversion[Math.floor(int / 100)] + ' Hundred';
            if (int % 100 === 0) return word
        }
        
        // Get tenth place
        if(int % 100 >= 20) {
            word += (word? ' ' : '' ) + num_word_conversion[Math.floor(int % 100 / 10) * 10];
        }
        
        // Special case for place between 10~19 
        // Return after this if-clause concatenation, since this covers the digit place
        if(int % 100 < 20){
            // console.log("decimal place", num_word_conversion[int % 10])
            word += (word? ' ' : '' ) + num_word_conversion[int % 100];       
            return word
        }
        
        if(int % 10 !== 0){
            word += (word? ' ' : '' ) + num_word_conversion[int % 10]
        }
        return word
    }
    
    // Input: between 1,000 <= num <= 999,999,999,999
    // Output: Partial English representation for num in thousandth, millionth, or billionth place
    // depending on <place>
    // e.g. 524,300 ==> Five Hundred Twenty Four Thousand 
    //      524,344,300 ==> Five Hundred Twenty Four Million 
    // etc.
    function large_numTE(num, place) {
        const suffix = num_word_conversion[place]
        
        var partial = Math.floor(num % (place*1000) / place);
        if(partial === 0){
            return ""  
        } else {
            // console.log(three_digit_conversion(partial) + ` ${suffix}`);
            return three_digit_conversion(partial) + ` ${suffix}`;
        }
    }

    var ans = "";
    const places = [1000000000, 1000000, 1000]
    
    for (const place of places) {
        let part = large_numTE(num, place);
        ans += part? part + ' ':'';
        // console.log(place, num, ans)
    }
    
    ans = ans + three_digit_conversion(Math.floor(num % 1000))
    
    return ans ? ans.trim() : "Zero" 
};