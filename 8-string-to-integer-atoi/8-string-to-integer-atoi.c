#include <stdio.h>
#include <ctype.h>
#include <limits.h>
#define MAX 2147483647
#define MIN -2147483648

long power(int base, int exp) {
    long ans = 1;
    for (int i = 0; i < exp; i++){
        if (ans * base > LONG_MAX){
            printf("Too long");
            return LONG_MAX;
        }
            
        ans *= (long)base;
    }
    return ans;
}

// check if a character is digit
int isDigit(char c) {
    return '0' <= c && c <= '9';
}


int myAtoi(char * s){
   for (;isblank(*s); s++) 
       ;
    
   int isNeg = 0;
   // inspect first charcter
   if(*s == '+' || *s == '-') {
     isNeg = *s++ == '-'; // check negativity and increment pointer    
   }
   
   // Starting reading digit
   char i; // tracks how many digits are read
   char digits[200]; // enough to hold all digits of any number < 2147483647 (2^31 - 1)
   for (i = 0;s[i] != '\0' && isDigit(s[i]);i++){
       digits[i] = s[i] - '0';
   }
    
   int j; // marks the first non-0 digit
   for (j = 0; j < i && digits[j] == 0; j++)
       ;
    
   long ans = 0;
   for (; j < i; j++){
       if((i - j - 1) >= 10){
           if (isNeg) return MIN;
           else return MAX;
           // ans = MAX;
           // printf("ans = %ld", ans);
           // break;
       }
       ans += digits[j] * power(10, i - j - 1);
       // printf("ans = %ld\n", ans);
   }
   
    
   // if is negative number flip the sign
   if(isNeg) {
       printf("Negative Number: %ld", ans);
       ans *= -1;
   }
     
   // clamping
   if (ans > MAX) 
       return MAX;
   else if(ans < MIN)
       return MIN;
    
   return ans;
}