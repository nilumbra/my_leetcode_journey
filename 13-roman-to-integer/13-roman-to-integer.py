class Solution:
    def romanToInt(self, s: str) -> int:
        table = self.rom_to_int()
        num = 0
        idx = 0
        while idx < len(s):
            if s[idx:idx+2] in table:
               num += table[s[idx:idx+2]]
               idx += 2
               continue
            else:
                num += table[s[idx]]
                idx += 1
        return num
            

    def rom_to_int(self):
        return {
             'I': 1,
             'V': 5,
             'IV': 4,
             'IX': 9,
              'X': 10,
              'L': 50,
             'XL': 40,
             'XC': 90,
              'C': 100,
              'D': 500,
             'CD': 400,
             'CM': 900,
               'M': 1000,
        }