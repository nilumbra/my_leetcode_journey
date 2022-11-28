void swap(char * a, char * b) {
  char t = *a;
  *a = *b;
  *b = t;
  // printf("%c, %c\n", *a, *b);
}

void getTrimIndex(char * s, int * start, int * end) {
  for (int i = 0; s[i] != '\0';i++) {
    if (s[i] != ' '){
      // always update end if curr char is not space, so that in the end,
      // `end` will always point to the last non-whitespace char
      *end = i; 
      if (*start == -1) { // set start to the index of first non-whitespace char
        *start = i;
      } 
    } else {
      // printf("%d,", *start);
      if (*start >= 0) { 
        
        int x = i;
        while (s[++x] == ' ')
          ;
        // next non-whitespace char
        int j = 0;
        while(s[x+j] != '\0' && s[x+j] != ' ') {
          swap(&s[i+j+1], &s[x+j]);
          j++;
        }
      }
    }
  }
}


void reverse(char * s, int start, int end) {
  for(;start < end; start++, end--) 
    swap(&(s[start]), &(s[end]));    
}


char * reverseWords(char * s){
  int start = -1, end = -1;
  getTrimIndex(s, &start, &end);
  s[end+1] = '\0';
  s = &(s[start]); 
  printf("%s", s);
  reverse(s, 0, end - start);
  
  int i, j;
  for (i = 0, j = 0; s[j] != '\0'; j++) {
    if(s[j+1] == ' ' || s[j+1] == '\0') {
      printf("%d, %d\n", i, j);
      reverse(s, i, j); // reverse a word
      i = j + 2;
      // printf("%s\n", s);
//       if (s[j+1] == '\0') { // end of string processing
//         while (s[++i] != '\0')
//           ;
//         s[i] = '\0';
//         break;
//       } else {

//         while (s[j+1] == ' ')
//           j++;
//       }
      
    }
  }
//   printf("%s\n", s);
//   printf("%c", s[j-1]);
  
  // printf("%c, %c", s[start], s[end]);
  return s;
}