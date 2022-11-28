#define square(n) (n) * (n)

int next(int n) {
  int s = 0;
  while (n > 0) {
    s += square(n % 10);
    n /= 10; 
  }
  
  return s;
}

bool isHappy(int n){
  printf("%d\n", next(1));
    
  int slow = next(n);
  int fast = next(next(n));
  
  if (slow == 1) return 1;
  else {
    while ((slow = next(slow)) != (fast = next(next(fast)))) 
      if (slow == 1) return 1;    
  }
  
  
  return slow == 1;
}