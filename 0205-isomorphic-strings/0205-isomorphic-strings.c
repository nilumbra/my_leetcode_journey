

bool isIsomorphic(char * s, char * t){
   int ms[255], mt[255];
   //printf("%u", strlen(s));
   //return false;
   for (int i = 0; i < 255; ++i) {
       //printf("%d", map[i]);
       ms[i] = -1;
       mt[i] = -1;
   }
   for (int i = 0; i < strlen(s); ++i) {
      // always replace s[i] with t[i]
      char a = s[i], b = t[i];
      
      if (ms[a] == -1) {
          if(mt[b] != -1) return false; 
          ms[a] = b;
          mt[b] = a;
      } else {
          if(ms[a] != b) return false;
      }
   }
   return true;
}