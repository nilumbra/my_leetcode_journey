var longestPalindrome = function(s) {
    const dp = new Array(s.length + 1).fill(0).map(()=>new Array(s.length + 1).fill(0));
        var m = -Infinity,
            cut = [0, 0];

    for (let j = 0; j <= s.length; j++) {
        for (let i = 0; i <= s.length; i++) {
            if (i + 1 >= j) {
                dp[i][j] = true;
            } else if (j - i == 2) {
                dp[i][j] = s[i] == s[j - 1];
                // if (dp[i][j]) {
                //     log("length 2 palindrome")
                //     log(`s.slice(${i}, ${j}) == ${s.slice(i, j)}`)
                // }
            } else {
                dp[i][j] = dp[i + 1][j - 1] && s[i] == s[j - 1];
            }

            if (dp[i][j] && (j - i) > m) {
                m = j - i;
                cut = [i, j];
            }
        }
    }

    return s.slice(...cut);
}