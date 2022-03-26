import math
def fullJustify(words, maxWidth):
    output = []
    startOfLine = 0
    endOfLine = 0
    line_len = 0
    # word_temp = []
    
    for i, word in enumerate(words):
        # word_temp.append(words[i])
        line_len += len(word) + 1

        endOfLine = i
        if (i + 1 == len(words)) or (endOfLine == startOfLine and (len(word) + 1 + len(words[i + 1])) > maxWidth): # last line or one-word line
            lastline = ""
            lastline__words = words[startOfLine: endOfLine + 1]
            trailing_space__num = maxWidth - sum(map(lambda x: len(x) + 1, lastline__words))
            for word in lastline__words:
                lastline = lastline + word + " "
            lastline += " " * trailing_space__num  
            # print(len(lastline))
            # assert(len(lastline) == maxWidth)

            output.append(lastline[:maxWidth])
            startOfLine = i + 1
            line_len = 0      
        elif line_len + len(words[i+1]) > maxWidth: #this line can accomodate up to current word

            #computing distribution of paddings
            paddings = get_paddings(words[startOfLine: endOfLine + 1], maxWidth)
            line = ""
            for j, word in enumerate(words[startOfLine:endOfLine]):
                line += word + " " * paddings[j]
            line += words[endOfLine]

            assert(len(line) == maxWidth)

            output.append(line)
            startOfLine = i + 1
            line_len = 0 

    return output

def get_paddings(words, maxWidth) :
        '''
        Let L = len(lengths), (assume L >= 2)
        then len(return value) will be (L - 1)
        '''
        num__words = len(words)
        paddings = [0] * (num__words - 1)
        length__words = sum(map(len, words))
        
        block = maxWidth - length__words
        return distribute(block, num__words - 1)
        
def distribute(block, slots):
    avg = block / slots
    if(block % slots == 0):
        return [int(avg)] * slots
    
    __first = math.ceil(avg) 
    return [__first] + distribute(block - __first, slots - 1)

if __name__ == '__main__':
    words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]

    maxWidth = 16


    print(fullJustify(words, maxWidth))