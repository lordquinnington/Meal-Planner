#~~~~~ Finds the size for the font and y position ~~~~~#


################################ meal suggestion box ################################

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


################################ week planner boxes ################################

def findPlanSize(chars,veggieMeal,vChars):
    if not veggieMeal:
        x1 = findPlanFontSize(chars)
        vx1 = None
        y1 = findPlanYSize(x1)
        vy1 = None

    else:
        x1 = findVPlanFontSize(chars)
        vx1 = findVPlanFontSize(vChars)
        y1 = findVPlanYSize(x1)
        vy1 = 33 + findVPlanYSize(vx1)

    return x1, y1, vx1, vy1
        
def findPlanFontSize(chars):
    x1 = 560/chars
    x2 = int(round(x1,0))
    if x2 > 65:
        return 65
    return x2

def findPlanYSize(size):
    y1 = size/2
    y2 = int(round(37-y1,0))
    if y2 < 0:
        return 0
    return y2

def findVPlanFontSize(chars):
    x1 = 300/chars
    x2 = int(round(x1,0))
    if x2 > 31:
        return 31
    return x2

def findVPlanYSize(size):
    y1 = size/2
    y2 = int(round(19-y1,0))
    if y2 < 0:
        return 0
    return y2


################################ meal by day box ################################

def findMBDSize(chars,veggieMeal,vChars):
    if not veggieMeal:
        x1 = findMBDFontSize(chars)
        vx1 = None
        y1 = findMBDYSize(x1)
        vy1 = None

    else:
        x1 = findVMBDFontSize(chars)
        vx1 = findVMBDFontSize(vChars)
        y1 = findVMBDYSize(x1)
        vy1 = 43 + findVMBDYSize(vx1)

    return x1, y1, vx1, vy1

def findMBDFontSize(chars):
    x1 = 560/chars
    x2 = int(round(x1,0))
    if x2 > 70:
        return 70
    return x2

def findMBDYSize(size):
    y1 = size/2
    y2 = int(round(40-y1,0))
    if y2 < 0:
        return 0
    return y2

def findVMBDFontSize(chars):
    x1 = 300/chars
    x2 = int(round(x1,0))
    if x2 > 31:
        return 31
    return x2

def findVMBDYSize(size):
    y1 = size/2
    y2 = int(round(20-y1,0))
    if y2 < 0:
        return 0
    return y2



