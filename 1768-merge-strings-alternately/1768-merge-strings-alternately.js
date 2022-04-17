/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    
    function zifu_xiangcanshu(word1, word2, left) {
        // 字符相参术
        if (word1.length == 0) {
            return word2
        }
    
        if (word2.length == 0) {
            return word1
        }
        
        if (left) {
            return word1[0] + zifu_xiangcanshu(word1.slice(1), word2, false)
        } else {
            return word2[0] + zifu_xiangcanshu(word1, word2.slice(1), true)
        }
    }
    
    return zifu_xiangcanshu(word1, word2, true)
};