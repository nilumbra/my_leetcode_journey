
// Algo:
// Let i = 0
// Walk through each character in <t> sequentially , if the currrent character = s[i]
// increment i
// Termination: 
// 1. string t is traversed exhaustively and i < s.length -> false
// 2. at any point, if i == s.length, -> true
bool isSubsequence(char * s, char * t){
    //int sLen = strlen(s);
    if (*s == '\0') return true;
    for (;*t != '\0';t++ ) {
        if (*s == *t) s++;
        if (*s == '\0') return true;
    }
    
    return false;
}