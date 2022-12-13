from collections import deque
class Solution:
  def calculate(self, s: str) -> int:
    def f(s):
      sign = '+'
      imdSt = []

      num = 0
      while len(s) > 0:
        c = s.popleft()
        if c.isdigit():
          num = 10 * num + int(c)
        
        if c == '(':
          num = f(s)

        if (c in ['+', '-', '*', '/', ')']) or len(s) == 0: 
          if sign == '+':
            imdSt.append(num)
          elif sign == '-':
            imdSt.append(-num)
          elif sign == '*':
            imdSt[-1] *= num
          elif sign == '/':
            imdSt[-1] = int(imdSt[-1] / float(num)) 

          # after the number is in stack, set:
          # the next sign as the current sign
          # reset the num
          sign = c
          num = 0
          
        if c == ')':
          # imdSt.append(num)
          return sum(imdSt)

      print(imdSt)
      return sum(imdSt)
    
    return f(deque(s))