from typing import List
from collections import defaultdict

# examine if currWord and target differ by only one charcater
def isConnected(currWord: str, target: str) -> bool:
    diff = 0
    for c1, c2 in zip(currWord, target):
        if c1 != c2: 
            diff += 1
        if diff > 1: 
            return False 
    return True if diff == 1 else False

class Problem:
    def __init__(self, beginWord:str, endWord: str, wordList: List[str]):
        self.beginWord = beginWord
        self.endWord = endWord
        self.wordList = set(wordList)
        self.parentGraph = { beginWord: None }
        self.explored = set()
        self.thisLevel = [beginWord]
        self.nextLevel = set()
        self.output = []

    def constructParentGraphWithBFS(self):
        while self.thisLevel:
            for word in self.thisLevel:
                # print(f'{word} has neighbors: {list(self.getNextLevel(word))}')
                for nei in self.getNextLevel(word):
                    self.nextLevel.add(nei)
                    if nei not in self.parentGraph:
                        self.parentGraph[nei] = [word]
                    else:
                        self.parentGraph[nei].append(word)
                self.explored.add(word) ## never explored {word} again

            if self.endWord in self.nextLevel:
                break
            # print(f'next level: {self.nextLevel}')
            self.thisLevel = list(self.nextLevel)
            self.nextLevel = set()

        # print(self.parentGraph)

            
    # Get the neighbors of currWord. Words that have been explored in previous levels are excluded
    def getNextLevel(self, currWord: str):
        for w in self.wordList:
            if w not in self.explored and w not in self.thisLevel and isConnected(currWord, w):
                yield w

    def constructAllShortestPaths(self):
        # start from endWord, walk throught the parentGraph until reaches beginWord
        # returns a list of walked path if endWord is in the parentGraph
        def backtrack(currWord, revTransSeq):
            if currWord is self.beginWord:
                self.output.append(reversed(revTransSeq))
                return
            else:
                for parent in self.parentGraph[currWord]:

                    backtrack(parent, revTransSeq + [parent])

        if self.endWord in self.parentGraph:
            backtrack(self.endWord, [self.endWord])

    def getAnswer(self):
        return self.output


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        problem = Problem(beginWord, endWord, wordList)
        problem.constructParentGraphWithBFS()
        problem.constructAllShortestPaths()

        return problem.getAnswer()