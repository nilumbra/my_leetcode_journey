# dynamic programming.  Time: O(n^2), Space: O(n^2) 
def longestPalindrome1(s: str) -> str:
  slen = len(s) 
  dp = [[False for i in range(slen)] for j in range(slen)]
  longest = [0, 0] # [i, j]
  longest_len = 1
  for i in reversed(range(slen)):
    for j in range(i, slen):
      dp[i][j] = (s[i]==s[j]) and ((j - i < 3) or dp[i+1][j-1])
      # if dp[i][j]: print(s[i:j+1])
      if dp[i][j] and ((j - i) + 1) > longest_len:
        longest[0],longest[1] = i, j
        longest_len = j - i + 1

  # print(longest)
  return s[longest[0]:longest[1]+1]

def longest_possible(center: int, leng: int) -> int:
  sym = max(2, 1 + min(abs(center + 1 - leng),center))
  pseudo = 2 + 2 * min(center, leng - 1 - center + 1)

  return max(sym, pseudo)

def maxPalindrome(s: str, longstr: int, left: int, right: int) -> str:
  res = ""
  while left >= 0 and right < len(s) and s[left] == s[right]:
    # if (left - 1) < 0 and (right + 1) >= len(s):
    #   break
    res = s[left:right+1]
    left -= 1
    right += 1

  # print(f'left:{left+1}, right:{right-1}')
  # print(f'{s[left+1:right]} v.s. {longstr}')

  if len(res) > len(longstr):
    return res

  return longstr

# Optimized(really?) centeral extension method(black magic)
def longestPalindrome2(s: str) -> str:
  if len(s) == 1: return s
  if len(s) == 2 and s[0] == s[1]: return s

  center = int(len(s)/2)
  _ = -1
  longest = [0, 0]
  res = ""
  while 0 <= center < len(s) and longest_possible(center, len(s)) > len(res):
    print(f'center: {center}')
    res = maxPalindrome(s, res, center, center)
    # print(f'res: {res}')
    res = maxPalindrome(s, res, center, center+1)
    center += _
    _ = -(_ + 1) if _ > 0 else -_ + 1

  # print(f'center: {center}, _: {_}')
  return res




