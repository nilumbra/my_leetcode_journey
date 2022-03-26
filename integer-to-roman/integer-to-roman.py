class Solution:
    def intToRoman(self, num: int) -> str:
        l = len(str(num))
        table = self.int_to_rom()
        place = lambda d: l - d - 1
        ans = ''
        for idx, d in enumerate(str(num)):
            d = int(d)
            if (place(idx), d) in table: 
                ans += table[(place(idx), d)]
                continue
            if d < 5:
                ans += table[place(idx)] * d
            else:
                ans += table[place(idx), 5] + table[place(idx)] * (d - 5)

        return ans
    
    def int_to_rom(self):
        return {
                    0: 'I',
                    (0, 5): 'V', 
                    (0, 4): 'IV',
                    (0, 9): 'IX',
                    1: 'X',
                    (1, 5): 'L', 
                    (1, 4): 'XL',
                    (1, 9): 'XC',
                    2: 'C',
                    (2, 5): 'D', 
                    (2, 4): 'CD',
                    (2, 9): 'CM',
                    3: 'M'
                }
    
    