class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        def isAlphabetical(w1, w2, t):
            if w1 == w2: return True
            if w1 == '': return True
            if w2 == '': return False
            
            if w1[0] == w2[0]:    
                return isAlphabetical(w1[1:], w2[1:], t)
            elif t[w1[0]] < t[w2[0]]:
                return True
            else:
                return False
            
                
            
        alien_alphabet = {}
        for idx, c in enumerate(order):
            alien_alphabet[c] = idx
        
        for i, word in enumerate(words[1:]):
            # print(word)
            if not isAlphabetical(words[i], word, alien_alphabet): return False
            
        return True
        