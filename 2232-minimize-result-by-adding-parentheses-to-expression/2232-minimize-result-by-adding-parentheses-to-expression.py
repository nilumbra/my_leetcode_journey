class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if len(expression) == 3:
            return '(' + expression + ')'

        def find_plus(exp):
            leftp, rightp = 0, 0
            for (idx,c) in enumerate(exp):
                if c == '+':
                    leftp, rightp = idx - 1, idx + 1
            return leftp, rightp
    
        leftpp, rightpp = find_plus(expression)
        smallest = float('inf')
        smallestIdx = [0, len(expression)]
        for leftp in range(0,leftpp+1):
            for rightp in range(rightpp, len(expression)):
                # print(leftp, rightp)
                left = int(expression[:leftp]) if expression[:leftp] != "" else 1
                middle = eval(expression[leftp: rightp+1])
                right = int(expression[rightp+1:]) if expression[rightp+1:] != "" else 1
                num = left * middle * right
                if num < smallest:

                    smallest = num
                    smallestIdx = [leftp, rightp]


        return expression[:smallestIdx[0]] + "(" + expression[smallestIdx[0]: smallestIdx[1]+1] + ")" + expression[smallestIdx[1]+1:]        