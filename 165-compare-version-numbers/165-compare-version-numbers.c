#include <stdio.h>

// int canEnd(char s, char t){
//     return s == '.' && 
// }

// If v points to an end of a revision, return 1, otherwise return 0 
int isRevEnd(char * v){
    if(v[0] == '\0' || *(v+1) == '\0' ||*(v+1) == '.'){ //|| *v == '.'
        return 1;
    }
    return 0;
}

// If *s is a leading 0, return 1, otherwise return 0
int isLeading0(char * s){
    if(*s == '.' || ((*s < '1' || *s > '9') && !isRevEnd(s))){ // If *s is 0 and s is not an end of revision, then *s is a leading 0
        return 1;
    }
    return 0;
}

int compareChar(char * s, char * t){
    char s1, s2;
    s1 = *s == '\0' ? '0' : *s;
    s2 = *t == '\0' ? '0' : *t;
    // printf("s1 = %c, s2 = %c\n", s1, s2);
    if (s1 - s2 == 0) 
        return 0;
    else 
        return s1 - s2 > 0 ? 1 : -1;
}
  
int compareVersion(char * version1, char * version2){
    // fast-forward version1 and version2 to first non leading 0
    int l1, l2; 
    do {
        // printf("*version1 = %c, *version2 = %c\n", *version1, *version2);
        l1 = isLeading0(version1);
        l2 = isLeading0(version2);
        if (l1) version1++;
        if (l2) version2++;
    } while(l1 || l2);

    // printf("\n");
    int e1, e2; // flag to mark whether version1 and version2 points to the end of revision
    int r1Greater = 0;
    do {
        // printf("*version1 = %c, *version2 = %c\n", *version1, *version2);
        e1 = isRevEnd(version1);
        e2 = isRevEnd(version2);
        
        // either of e1 or e2 reach the end of current revision
        // if e1 did not end, then e1 is bigger, otherwise e2 bigger
        if (e1 ^ e2) return e1 ? -1 : 1; 
        
        // either neither version1 or version2 are not the end of revision, or they are both ends of the revision
        
        // Determine the greatness of r1 and r2 in one shot(because digits to the right is more significant)
        if (r1Greater == 0) { 
            r1Greater = compareChar(version1, version2);
        }
        // if(!e1 && !e2) { // both has not ended
        //     version1++; 
        //     version2++;
        // }
        if(*version1 != '\0'){
          // printf("incrementing version1, current at: %s\n", version1);
          version1++;
        }
        
        if(*version2 != '\0'){
          // printf("incrementing version2, current at: %s\n", version2);
          version2++;
        }
            // continue to next iteration to further check
        // }
    }while(!e1 && !e2);
    // printf('\n');
       
    if(r1Greater != 0 || *version1 == '\0' && *version2 == '\0')
        return r1Greater;
    
    return compareVersion(version1, version2);
}

