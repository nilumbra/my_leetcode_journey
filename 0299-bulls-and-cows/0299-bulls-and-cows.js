/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    const map = {};
    var bull = 0, cow = 0;
    const bullSet = new Set();
  
    // find bull and account non-bull
    for (let i = 0; i < secret.length; ++i) {
      if (secret[i] == guess[i]) {
        bull++;
        bullSet.add(i);
      } else {
        if (secret[i] in map) 
          map[secret[i]]++;
        else 
          map[secret[i]] = 1;
      }
    }
    //console.log(map);
    // 
    for (let i = 0; i < secret.length; ++i) {
      if (!bullSet.has(i)) { // skip bull
         if (guess[i] in map && map[guess[i]] > 0) {
          map[guess[i]]--;
          cow++;
        }  
      }
    }
    
    return `${bull}A${cow}B`;
};