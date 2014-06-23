def getEstatus(x, y) :
    rx = x + 1
    ry = y
    if rx > (width - 1) :
        rx -= width
    return ref[ry][rx]

def getWstatus(x, y) :
    rx = x - 1
    ry = y
    if rx < 0 :
        rx += width
    return ref[ry][rx]

def getSstatus(x, y) :
    rx = x
    ry = y + 1
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]

def getNstatus(x, y) :
    rx = x
    ry = y - 1
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getNEstatus(x, y) :
    rx = x + 1
    ry = y - 1

    if rx > (width - 1) :
        rx -= width
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getNWstatus(x, y) :
    rx = x - 1
    ry = y - 1
    if rx < 0 :
        rx += width
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getSEstatus(x, y) :
    rx = x + 1
    ry = y + 1
    if rx > (width - 1) :
        rx -= width
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]

def getSWstatus(x, y) :
    rx = x - 1
    ry = y + 1
    if rx < 0 :
        rx += width
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]
