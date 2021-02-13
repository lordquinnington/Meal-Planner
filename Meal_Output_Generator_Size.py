#~~~~~ Finds the size for the font and y position ~~~~~#

def findSize(chars):
    return findFontSize(chars), findYSize(chars)

def findFontSize(chars):
    return 60-(int(round(chars/1.1,0)))

def findYSize(chars):
    return int(round(chars/2,0))
