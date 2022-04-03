import math
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        if(start == goal): return 0
        startb = "{0:b}".format(start)
        goalb = "{0:b}".format(goal)
        
        # print(startb, goalb)
        def flipIn3(s, g):
            print(s, g)
            c = 0
            for i in range(len(s)):
                if s[i] != g[i]:
                    c += 1

            return c

        
        diff = abs(len(goalb) - len(startb))

        if(goal > start):
            startb = "0" * diff + startb
            return flipIn3(startb, goalb)
        else:
            goalb = "0" * diff + goalb
            return flipIn3(startb, goalb)
            