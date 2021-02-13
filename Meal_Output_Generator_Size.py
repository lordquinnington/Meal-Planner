#~~~~~ Finds the size for the font and y position ~~~~~#

def findSize(chars):
    x1 = findFontSize(chars)
    y1 = findYSize(x1)
    return x1, y1

def findFontSize(chars):
    x1 = 580/chars
    x2 = int(round(x1,0))
    if x2 > 60:
        return 60
    return x2

def findYSize(size):
    y1 = size/2
    y2 = int(round(35-y1,0))
    if y2 < 0:
        return 0
    return y2
