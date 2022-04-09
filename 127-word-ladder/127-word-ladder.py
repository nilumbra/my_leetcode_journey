from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def all1Transformations(word):
            xf = set()
            for idx, char in enumerate(word):
                pre, su = word[:idx], word[idx + 1:]
                for _char in string.ascii_lowercase:
                    xf.add(pre + _char + su)
            
            return xf
        
        
        # BFS to find a least transformation sequence from beginWord to endWord
        agenda = deque()
        wordlist = set(wordList)
        agenda.append((beginWord, 1))
        
        
        if endWord not in wordlist: return 0 
        
        while agenda:
            curr_word, level  = agenda.popleft()
            for w in all1Transformations(curr_word):
                if w == endWord: return level + 1
                if w in wordlist:
                    wordlist.remove(w)
                    agenda.append((w, level+1))
        
        return 0
                
        